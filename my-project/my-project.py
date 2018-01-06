from airflow.hooks.postgres_hook import PostgresHook
import os
import pandas as pd

hook = PostgresHook('postgres_default')
conn = hook.get_conn()


query = """
SELECT 
	  tpep_pickup_datetime
	, passenger_count
	, trip_distance
	, total_amount
FROM nyc_taxi
LIMIT 10
"""
data = pd.read_sql(query, conn)
print(data)
