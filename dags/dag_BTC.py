import sys
from datetime import datetime, timedelta, timezone
from airflow.models import Variable
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

sys.path.append(
    '/home/vitalii/Documents/DataScience/My_Project/Project_v3_data_engineering/app')

from usdt_btc_init import insertRandomUSDT_BTC

default_args = {
    'owner': 'myuser',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 23, 13, 30, tzinfo=timezone.utc),
    'email': ['190293pvs@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG('dag_insert_usdt_btc', default_args=default_args, schedule_interval=timedelta(minutes=5), catchup=False) as dag:

    process_dag = PythonOperator(task_id='task_dag_insert_usdt_btc',
                                 python_callable=insertRandomUSDT_BTC)
