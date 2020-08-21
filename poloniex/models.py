from app import db
from datetime import datetime
from connection import conn

Base = declarative_base()

meta = MetaData(conn).reflect()

dwhConnection = conn.connect()
SessionDwh = sessionmaker(bind=dwhConnection)
sessionDwh = SessionDwh()

class Product(db.Model):
    __tablename__ = 'USDT_BTC'

    id = db.Column(db.Integer, primary_key=True)
    date_of_ticker = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last = db.Column(db.Float)
    lowestAsk = db.Column(db.Float)
    highestBid = db.Column(db.Float)
    percentChange = db.Column(db.Float)
    baseVolume = db.Column(db.Float)
    quoteVolume = db.Column(db.Float)
    isFrozen = db.Column(db.Float)
    high24hr = db.Column(db.Float)
    low24hr = db.Column(db.Float)


def initUSDT_BTC():
    isRun = False
    if not conn.dialect.has_table(conn, 'USDT_BTC'):
        Base.metadata.create_all(bind=conn)
        sessionDwh.commit()
        isRun = True
    return isRun


initUSDT_BTC()

sessionDwh.close()
dwhConnection.close()