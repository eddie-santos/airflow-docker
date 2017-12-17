# VERSION 1.0.0
# AUTHOR: Eddie Santos
# DESCRIPTION: Project 
# BUILD: docker build --rm -t esantos3/my-project:1.0.0 .
# SOURCE: https://github.com/esantos3/airflow-docker

FROM esantos3/airflow-base:latest
MAINTAINER Eddie Santos <eddie.santos.3@gmail.com>

ARG PROJECT_HOME=/usr/local/project

COPY ./requirements.txt ${PROJECT_HOME}/requirements.txt
RUN pip install -r ${PROJECT_HOME}/requirements.txt

COPY ./my-project.py ${PROJECT_HOME}/my-project.py

WORKDIR ${PROJECT_HOME}

CMD ["python", "my-project.py"]