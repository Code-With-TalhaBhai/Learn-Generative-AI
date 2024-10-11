
FROM python:3.11

WORKDIR /code

COPY . /code/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

CMD [ "poetry","run","uvicorn","app.main:app","--host","0.0.0.0","--reload" ]

EXPOSE 8000