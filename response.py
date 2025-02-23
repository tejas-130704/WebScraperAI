from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.gemini import Gemini
from llama_index.core import  StorageContext
import google.generativeai as genai
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from llama_index.core.schema import Document



def Response(index, question, llm):


    query_engine = index.as_query_engine(llm=llm)   
    response=query_engine.query(question).response
    return response

if __name__=="__main__":
    print("None")