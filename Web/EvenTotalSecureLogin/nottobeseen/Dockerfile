FROM ubuntu:14.04.5

RUN mkdir /app

WORKDIR /app
COPY . /app

RUN apt update &&  apt-get install libffi-dev build-essential libssl-dev python3-dev python3-pip -y

RUN pip3 install -r requirements.txt

