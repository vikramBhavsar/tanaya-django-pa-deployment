FROM python:3.8-slim
ENV SHELL=/bin/bash
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install build-essential bash \
  gcc \
  gettext \
  libffi-dev \
  libpq-dev\
  musl-dev \
  poppler-utils \
  postgresql-client \
  python3-dev \
  tcl-dev \
  tk-dev \
  netcat

RUN pip install pipenv
RUN pipenv run pip install --upgrade pip

ADD requirements.txt ./

RUN pipenv run python -m pip install -r requirements.txt

RUN mkdir /tanayaPortfolio
WORKDIR /tanayaPortfolio

EXPOSE 8000

ENTRYPOINT ["docker/scripts/init_api.sh"]
