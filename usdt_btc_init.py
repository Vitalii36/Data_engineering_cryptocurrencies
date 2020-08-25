from datetime import datetime
from sqlalchemy import DECIMAL, Column, DateTime, Integer, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connect import conn
import pandas as pd

Base = declarative_base()

meta = MetaData(conn).reflect()

dwhConnection = conn.connect()
SessionDwh = sessionmaker(bind=dwhConnection)
sessionDwh = SessionDwh()

class BTCTable(Base):
    __tablename__ = 'USDT_BTC'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_of_tiker = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    last = Column(Float())
    lowestAsk = Column(Float())
    highestBid = Column(Float())
    percentChange = Column(Float())
    baseVolume = Column(Float())
    quoteVolume = Column(Float())
    isFrozen = Column(Float())
    high24hr = Column(Float())
    low24hr = Column(Float())

    def __repr__(self):
        return "<BTCTable(name='%s')>" % (self.name)


df = pd.read_csv('~/Documents/DataScience/My_Project/Project_v3_data_engineering/app/csv/polonixinfo.csv', index_col  = 'Unnamed: 0')

def initTable():
    isRun = False
    if not conn.dialect.has_table(conn, 'USDT_BTC'):
        Base.metadata.create_all(bind=conn)
        sessionDwh.commit()
        isRun = True
    return isRun

def insertRandomUSDT_BTC(name_crt, df):
    prepareData = []
    Base.metadata.create_all(bind=conn)
    prepareData.append(BTCTable(
        last= float(df.at['last','BTC_BTS']),
        lowestAsk = float(df.at['lowestAsk','BTC_BTS']),
        highestBid = float(df.at['highestBid','BTC_BTS']),
        percentChange = float(df.at['percentChange','BTC_BTS']),
        baseVolume = float(df.at['baseVolume','BTC_BTS']),
        quoteVolume = float(df.at['quoteVolume','BTC_BTS']),
        isFrozen = float(df.at['isFrozen','BTC_BTS']),
        high24hr = float(df.at['high24hr','BTC_BTS']),
        low24hr = float(df.at['low24hr','BTC_BTS']),
    ))
    sessionDwh.add_all(prepareData)
    sessionDwh.commit()
    return True

initTable()
insertRandomUSDT_BTC('BTC_BTS', df)

sessionDwh.close()
dwhConnection.close()



