import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import VertexAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import AIMessage, HumanMessage

from src.utils import get_documents, split_documents, store_vectors
