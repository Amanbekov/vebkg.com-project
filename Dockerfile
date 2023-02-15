FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt/ /app/
ADD wsgi-entrypoint.sh /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . /app/