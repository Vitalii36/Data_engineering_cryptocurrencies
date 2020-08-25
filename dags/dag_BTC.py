import sys
from datetime import datetime, timedelta, timezone
from airflow.models import Variable
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'myuser',
    'depends_on_past': False,
    'email': ['190293pvs@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('dag_insert_usdt_btc', start_date=datetime(2020, 8, 25, 16, 0),
        end_date = datetime(2020, 8, 25, 16, 30),
        default_args=default_args, schedule_interval=timedelta(minutes=5), catchup = False) as dag:

    dag_insert_usdt_btc = BashOperator(task_id='dag_insert_usdt_btc',
                               bash_command='python ~/Documents/DataScience/My_Project/Project_v3_data_engineering/app/get_unit_polonixapi.py')

    dag_put_usdt_btc = BashOperator(task_id='dag_put_usdt_btc',
                                 bash_command='python ~/Documents/DataScience/My_Project/Project_v3_data_engineering/app/usdt_btc_init.py')

    dag_insert_usdt_btc >> dag_put_usdt_btc