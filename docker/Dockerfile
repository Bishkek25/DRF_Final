FROM python:3.10-slim

WORKDIR /urs/src/app

COPY ../requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .