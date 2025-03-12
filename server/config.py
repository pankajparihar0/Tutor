from pinecone import Pinecone
from google import genai
from langchain.text_splitter import CharacterTextSplitter

def conn_pinecorn():
    pc = Pinecone(api_key="key")
    return pc
def conn_gemini():
    client = genai.Client(api_key="AIzaSyBgXP2bVvfozVblBy9_fwJL4AIl5IcGBm4")
    return client