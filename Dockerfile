FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY builds builds

COPY src src

WORKDIR src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
