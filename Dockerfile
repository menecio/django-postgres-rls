FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONBREAKPOINT=ipdb.set_trace

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update --yes && \
  apt-get install --no-install-recommends --yes curl build-essential libpq-dev postgresql-client && \
  pip install -r /app/requirements.txt --no-cache-dir --disable-pip-version-check && \
  rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app/demo

EXPOSE 8001

CMD /app/demo/manage.py runserver 0.0.0.0:8000
