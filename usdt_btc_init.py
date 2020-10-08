from datetime import datetime
from sqlalchemy import DECIMAL, Column, DateTime, Integer, MetaData, Float
from sqlalchemy.orm import sessionmaker
from connect import conn
import pandas as pd
from models import Base, list_table, BTCTable, ZECTable, ETHTable, XMRTable, ETCTable, DASHTable, LTCTable

meta = MetaData(conn).reflect()

dwhConnection = conn.connect()
SessionDwh = sessionmaker(bind=dwhConnection)
sessionDwh = SessionDwh()

df = pd.read_csv('~/Documents/DataScience/My_Project/Project_v3_data_engineering/app/csv/polonixinfo.csv', index_col  = 'Unnamed: 0')

def initTable(name_crt):
    isRun = False
    if not conn.dialect.has_table(conn, name_crt):
        Base.metadata.create_all(bind=conn)
        sessionDwh.commit()
        isRun = True
    return isRun

def insert_USDT_crt(name_crt, df, name_t_class):
    prepareData = []
    Base.metadata.create_all(bind=conn)
    prepareData.append(name_t_class(
        last= float(df.at['last',name_crt]),
        lowestAsk = float(df.at['lowestAsk',name_crt]),
        highestBid = float(df.at['highestBid',name_crt]),
        percentChange = float(df.at['percentChange',name_crt]),
        baseVolume = float(df.at['baseVolume',name_crt]),
        quoteVolume = float(df.at['quoteVolume',name_crt]),
        isFrozen = float(df.at['isFrozen',name_crt]),
        high24hr = float(df.at['high24hr',name_crt]),
        low24hr = float(df.at['low24hr',name_crt]),
    ))
    sessionDwh.add_all(prepareData)
    sessionDwh.commit()
    return True

for i in list_table.keys():
    initTable(list_table[i])
    insert_USDT_crt(list_table[i], df, i)


sessionDwh.close()
dwhConnection.close()



