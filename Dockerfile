FROM python:3.6

RUN apt update
RUN apt install -y postgresql-client vim

RUN mkdir /app/
WORKDIR /app/
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
