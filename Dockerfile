FROM python:3.9-slim-buster

WORKDIR /app

COPY skrypt.py /app/skrypt.py

ENTRYPOINT [ "python", "/app/skrypt.py" ]