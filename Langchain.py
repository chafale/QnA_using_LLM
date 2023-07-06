# Q/A Over a PDF File using Langchain and LLMS


import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import tempfile
from bokeh.models import Box

os.environ['OPENAI_API_KEY']="YOUR API KEY"  # Using the OPEN AI API key here

def qa(file, query, chain_type, k):
    
    loader = PyPDFLoader(file)  # load document
    documents = loader.load()
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0) # split the documents into chunks
    texts = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()   # selecting the type of embeddings
    
    # create the vectorestore to use as the index
    # Chroma is an open source vector database alternative to Pinecone DB
    db = Chroma.from_documents(texts, embeddings)
    
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k}) # expose this index in a retriever interface
    
    # create a chain to answer questions 
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type=chain_type, retriever=retriever, return_source_documents=True)
    result = qa({"query": query})
    return result

query=input("Enter your query")
result = qa("C:/Users/asus/Desktop/involveAI/Q1-2023-PFE-Earnings-Release.pdf", query,"stuff",3)  # Passing the path to pdf file
if result['result']==" I don't know.":  # if response is I dont know then pass to LLM
    llm=OpenAI()
    print (llm(query))
else:
    print (result['result'])

 

