FROM python:3.8-slim-buster



WORKDIR /app

COPY Pipfile Pipfile.lock /app/


# system applications
RUN apt update && apt install libpq-dev gcc -y

RUN pip install pipenv && pipenv install --system

