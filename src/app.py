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
