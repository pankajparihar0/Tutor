from fastapi import APIRouter,File
from data_insertion import inset_data

router = APIRouter()
@router.post("/upload")
async def query(Class: int ,book:str ,chapter : str,):
    return inset_data("./Data/Raw/iesc101.pdf",book,chapter,Class)