FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/fastapi_app

COPY ./fastapi_app/requirements.txt .

RUN useradd -U app && mkdir -p /app && chown -R app:app /app

RUN pip install -r ./requirements.txt

COPY ./fastapi_app/ .

ENV PYTHONPATH "${PYTHONPATH}:/app/fastapi_app/"
