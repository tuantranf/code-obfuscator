FROM python:3.7.0-alpine3.8

MAINTAINER podder.ai <https://github.com/podder-ai>

RUN apk add --virtual .build-deps gcc musl-dev

COPY entrypoint.sh /entrypoint.sh

ADD requirements.txt /usr/local/code-obfuscator/

WORKDIR /usr/local/code-obfuscator

RUN pip install -r requirements.txt

ADD . /usr/local/code-obfuscator

RUN mkdir /source

ENTRYPOINT ["sh", "/entrypoint.sh"]