FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN mkdir -p /tmp/RadonCTT
VOLUME /tmp/RadonCTT

COPY requirements.txt /usr/src/app/

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget git
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]
