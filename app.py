import google.generativeai as genai
import streamlit as st
import requests
#Import llms from llama_index
from llama_index.llms.openai import OpenAI
from llama_index.llms.gemini import Gemini
from llama_index.llms.deepseek import DeepSeek
from llama_index.llms.groq import Groq

from preprocessing_data import preprocess_data
from llama_index.core.schema import Document
from response import Response
from llama_index.core import VectorStoreIndex
from llama_index.llms.gemini import Gemini
from llama_index.core import  StorageContext
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.schema import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding

# gemini_embed_model=GeminiEmbedding(model_name="models/embedding-001")
# Sidebar for model selection and API key input
st.sidebar.title("LLM Model Selection")
model_type = st.sidebar.selectbox("Select Model", ["OpenAI GPT-3.5", "OpenAI GPT-4", "Gemini Pro", "Gemini Ultra", "DeepSeek","Groq"])
api_key = st.sidebar.text_input("Enter API Key", type="password")
# Input for website link
website_url = st.sidebar.text_input("Enter Website URL")
is_deep = st.sidebar.checkbox("Use Deep Analysis")

# if "OpenAI" in model_type:
#     embed_model = OpenAIEmbedding(api_key=api_key)  # Use OpenAI embeddings
# elif "Gemini" in model_type:
#     embed_model = GeminiEmbedding(model_name="models/embedding-001")  # Use Gemini embeddings
# else:
#     embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Default Hugging Face embeddings



embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")


# Main UI for question-answering
# st.title("WebScaperAI")
st.title("Website Q&A Playground")
question = st.text_input("Ask a question about the website content")





# Button to load website and LLM model
if st.sidebar.button("Load Website & LLM"):
    if not api_key or not website_url:
        st.warning("Please enter API key and website URL.")
    else:
        st.info("Loading website content and initializing LLM...")
        website_content = preprocess_data(website_url,is_deep)
        doc = [Document(text=website_content)]
        # print(doc)
        # a vector store index only needs an embed model
        index = VectorStoreIndex.from_documents(
            doc, embed_model=embed_model, name="my_index"
        )
        st.session_state["index"] = index
        # Initialize LLM model based on selection
        if model_type in ["OpenAI GPT-3.5", "OpenAI GPT-4"]:
            llm = OpenAI(
                model_name="gpt-3.5-turbo" if model_type == "OpenAI GPT-3.5" else "gpt-4",
                api_key=api_key
            )
        elif model_type in ["Gemini Pro", "Gemini Ultra"]:
            genai.configure(api_key=api_key)  # Configure API key for Google Gemini
            llm = Gemini(
                model_name="models/gemini-pro" if model_type == "Gemini Pro" else "gemini-ultra-1.0",
                api_key=api_key
            )


        elif model_type == "DeepSeek":
            llm = DeepSeek(model="deepseek-chat", api_key=api_key)
            
        elif model_type == "Groq":
            llm = Groq(model="llama3-70b-8192", api_key=api_key)
        else:
            llm = None  # You can define your custom model logic here

        st.session_state["llm"] = llm
        st.session_state["website_content"] = website_content
        st.success("Website content loaded and LLM initialized.")

# Info message
st.sidebar.info("ℹ️ Using Deep Analysis may take longer to process. Because it will scrape all the revalent links from the website. ℹ️ Deep Analysis is only recommended for limited scope (smaller) websites.")

# Button to ask questions
if st.button("Ask Question"):
    if "llm" not in st.session_state or "website_content" not in st.session_state:
        st.warning("Please load the website and LLM first.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        st.info("Processing your question...")
        llm = st.session_state["llm"]
        website_content = st.session_state["website_content"]
        if "index" not in st.session_state:
            st.warning("Please load the website and LLM first.")
        else:
            index = st.session_state["index"]  # Retrieve index from session state
            response = Response(index, question, llm)
        st.success(response)
