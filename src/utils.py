import os
import shutil
import tempfile

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import VertexAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from streamlit.runtime.uploaded_file_manager import UploadedFile
from langchain.schema import Document
from typing import List

def get_documents(pdf_file: UploadedFile) -> List[Document]:
    """ Function that read pdf and return pages as a list of documents

    Args:
        pdf_file (UploadedFile): File uploaded by the user

    Returns:
        List[Document]: list of langchain documents
    """


    # Temporary directory
    temp_dir = tempfile.TemporaryDirectory()
    # Generate a temporary file path
    temp_file_path = tempfile.NamedTemporaryFile(dir=temp_dir.name).name
    # Save the pdf file in the temporary file path
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(pdf_file.read())

    # Load the pdf file
    loader = PyPDFLoader(temp_file_path)

    # Return the documents
    docs = loader.load()

    # Clean up
    temp_dir.cleanup()

    return docs


def split_documents(docs: List[Document], chunk_size: int, chunk_overlap: int) -> List[Document]:
    """Split documents into chunks

    Args:
        docs (List[Document]): list of documents
        chunk_size (int): chunk size
        chunk_overlap (int): chunk overlap allowed

    Returns:
        chunks (List[Document]): List of chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = text_splitter.split_documents(docs)

    return chunks

def store_vectors(chunks: List[Document], project_id:str, persist_directory: str):
    """Create vector store and store chunks as vectors

    Args:
        chunks (List[Document]): list of chunks
        project_id (str): GCP project Id
        persist_directory (str): directory to store the vector store

    Returns:
        vectordb (Chroma): Chroma Database
    """    
    # Load embeddings
    embeddings = VertexAIEmbeddings(project=project_id)

    # Clean chroma persist directory if exists
    if os.path.isdir(persist_directory):
        shutil.rmtree(persist_directory, ignore_errors=True)

    # Create Vector Store
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
    # Save in memory
    vectordb.persist()

    return vectordb
