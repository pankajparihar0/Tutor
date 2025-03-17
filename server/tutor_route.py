from fastapi import APIRouter

from tutor_service import TutorService

tutor_service = TutorService()

router = APIRouter()

@router.post("/query")
async def query(question: str):
    # return "hello"
    # question ="what is Corrosion"
    return tutor_service.get_question_answer(question)

@router.post("/quiz")
async def query(topic : str,number:int):
    return tutor_service.get_quiz(topic,number)
    return "helllllo"