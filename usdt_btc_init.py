from datetime import datetime
from random import randrange

from sqlalchemy import DECIMAL, Column, DateTime, Integer, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from connect import conn

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

def initTable():
    isRun = False
    if not conn.dialect.has_table(conn, 'USDT_BTC'):
        Base.metadata.create_all(bind=conn)
        sessionDwh.commit()
        isRun = True
    return isRun


def insertRandomUSDT_BTC():
    prepareData = []
    Base.metadata.create_all(bind=conn)
    prepareData.append(BTCTable(
        last= randrange(1, 1000),
        lowestAsk= randrange(1, 1000),
        highestBid= randrange(1, 1000),
        percentChange= randrange(1, 1000),
        baseVolume= randrange(1, 1000),
        quoteVolume= randrange(1, 1000),
        isFrozen= randrange(1, 1000),
        high24hr= randrange(1, 1000),
        low24hr= randrange(1, 1000)
    ))
    sessionDwh.add_all(prepareData)
    sessionDwh.commit()
    return True


initTable()
insertRandomUSDT_BTC()

sessionDwh.close()
dwhConnection.close()