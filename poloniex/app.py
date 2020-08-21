from airflow.models import Variable
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from constans import DB_URL

db = SQLAlchemy()

connection = create_engine(DB_URL, echo=False)
conn = connection.connect()