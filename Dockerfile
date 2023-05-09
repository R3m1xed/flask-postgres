FROM python:3.9.16-bullseye

RUN pip install --upgrade pip

RUN apt-get update && apt-get install apt-transport-https -y

WORKDIR /docker-flask-test

ADD ./app /docker-flask-test

#python packages needed to make this work
RUN pip install flask
RUN pip install psycopg2-binary

#Makes sure that the flask app runs upon starting
CMD ["python", "view.py"]
