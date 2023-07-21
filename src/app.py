import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import VertexAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage, HumanMessage

from src.utils import get_documents, split_documents, store_vectors


### APP ###
def app(project_id, model_name, chunk_size, chunk_overlap, persist_directory):
    st.title("📩 CV Reviewer")

    with st.sidebar:
        st.header("Choose your avatar:")
        user_avatar = st.radio("Avatar", ["👨‍⚕️", "👩‍⚕️", "👽"])
        st.header("Upload yout CV here")
        uploaded_file = st.file_uploader("Upload a CV", type="pdf")
        if uploaded_file:
            # Just load documentes if they have not been loaded before
            if "qa" not in st.session_state:
                with st.spinner("Loading document..."):
                    # Get the documents
                    docs = get_documents(uploaded_file)

                    # Split documents
                    chunks = split_documents(docs, chunk_size, chunk_overlap)

                    # Store chunks as embeddings
                    vectordb = store_vectors(chunks, project_id, persist_directory)

                    # Create Memory
                    memory = ConversationBufferMemory(
                        memory_key="chat_history", return_messages=True
                    )

                    # st.session_state['memory'] = memory

                    # LLM
                    llm = VertexAI(model=model_name, project_id=project_id)
                    # Retriever
                    retriever = vectordb.as_retriever()
                    # Conversational Chain
                    qa = ConversationalRetrievalChain.from_llm(
                        llm, retriever=retriever, memory=memory
                    )
                    st.session_state["qa"] = qa

    if uploaded_file is None:
        with st.chat_message("assistant"):
            st.write("Please upload your CV")
    else:
        prompt = st.chat_input("Ask something")
        if prompt:
            # Answer
            answer = st.session_state["qa"]({"question": prompt})
            # Load History messages (this includes the answer)
            for message in answer["chat_history"]:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user", avatar=user_avatar):
                        st.write(message.content)
                elif isinstance(message, AIMessage):
                    with st.chat_message("assistant", avatar="🤖"):
                        st.write(message.content)
