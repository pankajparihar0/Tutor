from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pinecone import Pinecone
from google import genai
from reg_service import LLMresponce
from tutor_route import router as tutor_router



app = FastAPI()


# client = genai.Client(api_key="AIzaSyBgXP2bVvfozVblBy9_fwJL4AIl5IcGBm4")
# pc = Pinecone(api_key="pcsk_6EY2n1_CAkXxUGGeuniBFAF3pJT9WcB5GLXNXdHiWvnvZwyTa9w4gW7aKWGqZxwcQRrWy")
# index_name = "dense-index" 
# query = "steps to balance a chemical equation"


# def LLMresponce():
#     dense_index = pc.Index(index_name)
#     results = dense_index.search(
#     namespace="example-namespace",
#     query={
#         "top_k": 5,
#         "inputs": {
#             'text': query
#         }
#     }
#     )
#     llmtext = ""
#     for hit in results['result']['hits']:
#         llmtext = llmtext +" "+hit['fields']['chunk_text']

#     prompt = f"""you are a joiner teacher in a government school having exprience of 10 year in teaching.currently you are teaching class 8th student.answer the
#     question delimitted by double backticks and the context for the quesition is delimitted by triple backticks.do not use your own knowledge and keepit sort
#     question :''{query}'' \n
#     context : '''{llmtext} '''
#     """

#     response = client.models.generate_content(
#         model="gemini-2.0-flash", contents=prompt
#     )

#     return response.text


app.include_router(tutor_router, prefix="/tutor")

@app.get("/")
async def get():
    # answer = LLMresponce()
    return {"message": "hiii"}

