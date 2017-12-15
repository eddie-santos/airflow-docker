# Running Airflow via Docker

This work is built on top of the `puckel/docker-airflow` base image created by Matthieu Roisil, of which the repo can be find [here](https://github.com/puckel/docker-airflow).

The work presented here differents in that it instructs the users how to create Airflow in a production environment, storing metadata in an external database, and using Docker Compose to manage the number of workers.

Steps:
1. Clone this repo.
2. Create a **{environment-name}.env**  (e.g. local.env, dev.env, prod.env) file in the base directory that contains all of your environment variables in `ENVIRONMENT_VARIABLE=variable` format.
3. Type `docker build --rm -t repo/image:tag .` to build the image.
4. Type `docker run -d -p 8080:8080 --env-file={environment-name.env} repo/image:tag` to run your image.


### Build

```bash
docker build --rm \
--build-arg SQL_ALCHEMY_CONN=$SQL_ALCHEMY_CONN \
--build-arg FERNET_KEY=$FERNET_KEY \
--build-arg BROKER_URL=$BROKER_URL \
-t esantos3/airflow-base:1.0.0 .
```


### Configurations with environment variables

To run Airflow inside a container, we need a metadata database outside of the container to track state. Typically, 
these variables live inside of **config/airflow.cfg**, though it's bad practice to store sensitive credentials in a 
file that will be stored in a repository (e.g. [Uber](https://www.bloomberg.com/news/articles/2017-11-21/uber-concealed-cyberattack-that-exposed-57-million-people-s-data)). 
Instead, we can store them as environment variables, or list them in a file, here denoted as **{environment-name}.env**, in which
we can load them as environment variables inside of the Docker container.

The relevant variables inside the config file to set are the following, using the `AIRFLOW__{SECTION}__{KEY}` format:
- **sql_alchemy_conn**: connection string for SQL Alchemy to reach the metadata database. Can be set via `AIRFLOW__CORE__SQL_ALCHEMY_CONN`. For example, using PostgreSQL, the metadata database can be hit with the configuration, `AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://user:password@host:5432/database`. 

For running on PostgreSQL at `localhost`, note that the user most use `docker.for.mac.localhost` as the host instead of `localhost`, since otherwise Docker will assume that PostgreSQL is running inside the container. Otherwise, **host** should be the ip address the database resides at. 

_Note: change **user**, **password**, and **database** to something less obvious, though it is standard to keep the default PostgresSQL port of `5432`_.

- **remote_base_log_folder**: remote folder to store log files, using AWS S3 or Google Cloud, for example. It can be set via `AIRFLOW__CORE__REMOTE_BASE_LOG_FOLDER=s3://path/to/your/bucket`, using S3. Using the default configuration will store all Airflow logs inside of the container, which will be wiped out whenever the container is stopped. Using S3 provides a cheap and efficient way to collectively store logs across containers.

- **remote_log_conn_id**: remote file store Airflow connection Conn Id, in the format `AIRFLOW__CORE__REMOTE_LOG_CONN_ID=s3_default`, using S3 with the **s3_default** Conn Id, for example.

### Using Docker Compose and Swarm to manage cluster size