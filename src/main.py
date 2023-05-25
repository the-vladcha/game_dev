from fastapi import FastAPI
from tasks.router import router as router_tasks

app: FastAPI = FastAPI()

app.include_router(
    router_tasks,
    prefix='/tasks',
    tags=['Tasks']
)
