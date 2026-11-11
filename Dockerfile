FROM python:3.12-slim

WORKDIR /app

COPY app.py ./

ENV APP_NAME=World

CMD ["python", "app.py"]
