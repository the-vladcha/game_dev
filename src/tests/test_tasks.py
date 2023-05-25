import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_get_tasks():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/tasks/get_tasks/", json={'build': 'write_beautiful'})
    assert response.status_code == 200
    # assert response.json() == {"message": "Tomato"}
