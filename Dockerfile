FROM python:3.9.16-bullseye

RUN pip install --upgrade pip

RUN apt-get update && apt-get install libmariadb3 libmariadb-dev apt-transport-https -y

WORKDIR /docker-flask-test

ADD ./app /docker-flask-test

#RUN mkdir mariadb-connector-python && cd mariadb-connector-python && tar -xvzf ../mariadb-connector-python-1.1.6.tar.gz

#RUN pip3 install /docker-flask-test/mariadb-connector-python/mariadb-*

#WORKDIR /docker-flask-test
RUN pip install flask
RUN pip install psycopg2-binary
#RUN pip install mysql-connector-python pandas
#RUN pip install mariadb
#RUN pip install mariadb==3.1.20

#RUN pip install -r requirements.txt

CMD ["python", "view.py"]
