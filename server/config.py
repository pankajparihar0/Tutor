from pinecone import Pinecone
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

def conn_pinecorn():
    pc = Pinecone(api_key=os.getenv('PINECORN_KEY'))
    return pc
def conn_gemini():
    client = genai.Client(api_key=os.getenv('gemini_key'))
    return client