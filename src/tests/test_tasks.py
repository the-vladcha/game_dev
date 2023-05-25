import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_get_tasks():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/tasks/get_tasks/", json={'build': 'write_beautiful'})
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_tasks_with_error():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/tasks/get_tasks/", json={'build': 'qwerty'})
    assert response.status_code == 500


@pytest.mark.anyio
async def test_get_tasks_error_with_wrong_body():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/tasks/get_tasks/", json={'name': 'qwerty'})
    assert response.status_code == 422
