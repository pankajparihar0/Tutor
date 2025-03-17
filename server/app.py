from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tutor_route import router as tutor_router
from upload_route import router as upload_router
from data_insertion import inset_data


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tutor_router, prefix="/tutor")
app.include_router(upload_router, prefix="/upload")

# # You can now process the result if needed
@app.get("/")
async def get():
    return "hii"

