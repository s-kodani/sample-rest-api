FROM python:alpine3.14

WORKDIR /usr/src/app

ENV DOCKERIZE_VERSION v0.6.1

COPY . .

RUN apk add --no-cache openssl gcc g++ libffi-dev curl \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN python -m pip install -U pip \
 && pip install -U --no-cache-dir poetry
RUN ls ./
RUN poetry install --no-dev

CMD [ "poetry", "run", "python", "sample_rest_api/run.py" ]