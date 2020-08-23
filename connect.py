from airflow.models import Variable
from sqlalchemy import create_engine

host = Variable.get('host', '0.0.0.0:5432')
db_name = Variable.get('db_name', 'mydb')
username = Variable.get('username', 'myuser')
password = Variable.get('password', 'pass')

connection = create_engine('postgresql+psycopg2://{username}:{password}@{url}/{db_name}'
                           .format(username=username, password=password,
                                   url=host, db_name=db_name))
conn = connection.connect()