# VERSION 1.0.0
# AUTHOR: Eddie Santos
# DESCRIPTION: Basic Airflow container
# BUILD: docker build --rm -t esantos3/airflow:1.0.0 .
# SOURCE: https://github.com/esantos3/airflow-docker

FROM esantos3/airflow-base:1.0.0
MAINTAINER Eddie Santos <eddie.santos.3@gmail.com>

ARG AIRFLOW_HOME=/usr/local/airflow
COPY dags ${AIRFLOW_HOME}/dags

EXPOSE 8080 5555 8793

CMD ["airflow", "webserver"]