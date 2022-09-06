FROM python:3.8.5-slim-buster

WORKDIR /usr/src/app

RUN pip install pipenv==v2021.5.29 --no-cache-dir
COPY Pipfile* ./
#por alguna razón el uvicorn no se está instalando en el pipenv install pero SÍ está en los requirements.
RUN pip install uvicorn
RUN pipenv install --dev --system --deploy
RUN pipenv install

COPY . .
#EXPOSE 80