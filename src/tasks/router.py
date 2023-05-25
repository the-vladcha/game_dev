from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from tasks.schemas import Item
from tasks.service import TasksGenerator

router = APIRouter(
    prefix='/get_tasks'
)


@router.post('/')
async def get_tasks(build: Item) -> JSONResponse:
    try:
        return JSONResponse(jsonable_encoder(TasksGenerator().get_tasks(build.build)))
    except Exception as er:
        return JSONResponse(content=jsonable_encoder({'error': er}), status_code=500)
