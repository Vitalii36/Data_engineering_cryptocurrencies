from sqlalchemy import DECIMAL, Column, DateTime, Integer, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

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

class ZECTable(Base):
    __tablename__ = 'USDT_ZEC'

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
        return "<ZECTable(name='%s')>" % (self.name)

class ETHTable(Base):
    __tablename__ = 'USDT_ETH'

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
        return "<ETHTable(name='%s')>" % (self.name)

class XMRTable(Base):
    __tablename__ = 'USDT_XMR'

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
        return "<XMRTable(name='%s')>" % (self.name)

class ETCTable(Base):
    __tablename__ = 'USDT_ETC'

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
        return "<ETCTable(name='%s')>" % (self.name)

class DASHTable(Base):
    __tablename__ = 'USDT_DASH'

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
        return "<DASHTable(name='%s')>" % (self.name)

class LTCTable(Base):
    __tablename__ = 'USDT_LTC'

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
        return "<LTCTable(name='%s')>" % (self.name)

list_table = {BTCTable:'USDT_BTC' ,ZECTable:'USDT_ZEC' ,ETHTable:'USDT_ETH'
    ,XMRTable:'USDT_XMR' ,ETCTable:'USDT_ETC' ,DASHTable:'USDT_DASH' ,LTCTable:'USDT_LTC'}
