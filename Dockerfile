FROM python:3.7-alpine
MAINTAINER Mohan

ENV PYTHONUNBUFFERRED 1

COPY ./requirements.txt /requirements.txt
#copy the requirements.txt file in the ubuntu system(local) to the requirements.txt inside the docker image

RUN pip install -r /requirements.txt

RUN mkdir /app
#create a directory called /app inside the docker image

WORKDIR /app
#make the dir /app as the working directory inside the docker image

COPY ./app/ /app
#copy the content from /app dir in the local machine to the /app folder of the docker image

RUN adduser -D user
#creates an user called "user" and provides permission for the user to run only the application (-D)

USER user
#makes the current user as the user


