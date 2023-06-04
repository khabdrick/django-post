FROM python:3.9.2

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal    

RUN pip install django psycopg2-binary

RUN mkdir /project
WORKDIR /project

COPY . .