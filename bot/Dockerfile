FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/monitor/

COPY ./bot/requirements.txt .

RUN useradd -U app && mkdir -p /app && chown -R app:app /app

RUN pip install -r ./requirements.txt

COPY ./bot/ .

ENV PYTHONPATH "${PYTHONPATH}:/app/bot/"

CMD ["sh", "-c", "python3 ./main.py"]
