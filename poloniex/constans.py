import os


host = Variable.get("0.0.0.0:5432")
db_name = Variable.get("mydb")
username = Variable.get("myuser")
password = Variable.get("pass")

# DB_URL =  os.environ['DB_URL']
DB_URL = 'postgresql+psycopg2://{username}:{password}@{url}/{db_name}?charset=utf8'.format(username=username,
                                                                                           password=password,
                                                                                           url=host, db_name=db_name)