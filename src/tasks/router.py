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
    return JSONResponse(jsonable_encoder(TasksGenerator().get_tasks(build.build)))
