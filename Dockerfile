# pull official base image
FROM python:3.10.1-alpine

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN apk update && apk add tk
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN pip install --upgrade pip
RUN apk add libffi-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .