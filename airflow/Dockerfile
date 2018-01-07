# VERSION 1.0.0
# AUTHOR: Eddie Santos
# DESCRIPTION: Basic Airflow container
# BUILD: docker build --rm -t esantos3/airflow.
# SOURCE: https://github.com/esantos3/airflow-docker
# LINK: https://docs.docker.com/engine/installation/linux/docker-ce/centos/

FROM esantos3/airflow-base:latest
MAINTAINER Eddie Santos <eddie.santos.3@gmail.com>

ARG AIRFLOW_HOME=/usr/local/airflow

ENV AIRFLOW_HOME=${AIRFLOW_HOME}

RUN apt-get update -yqq \
    && apt-get install -yqq \
    	apt-transport-https \
    	ca-certificates \
    	curl \
    	gnupg2 \
    	software-properties-common \
    && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - \
    && add-apt-repository \
   		"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    	$(lsb_release -cs) \
    	stable" \
    && curl -fsSL https://get.docker.com/ | sh \
    && pip install docker \
    && pip install docker-py

COPY dags ${AIRFLOW_HOME}/dags

EXPOSE 8080 5555 8793

WORKDIR ${AIRFLOW_HOME}

CMD ["airflow", "scheduler"]

CMD ["airflow", "webserver"]