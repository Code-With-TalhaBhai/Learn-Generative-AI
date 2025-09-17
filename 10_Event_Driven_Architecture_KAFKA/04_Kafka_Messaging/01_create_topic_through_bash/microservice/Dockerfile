FROM python:3.12

WORKDIR /code

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /code/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

CMD [ "poetry", "run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload" ]

EXPOSE 8000


