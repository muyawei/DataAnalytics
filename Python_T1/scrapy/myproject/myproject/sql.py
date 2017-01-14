# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, Boolean
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql://root:123456@10.18.99.126:3306/test", echo=True)

# 获得Base
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Agency(Base):
    __tablename__ = "agency"
    id = Column(INTEGER, primary_key=True)
    province = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    count = Column(INTEGER)
    address = Column(String(50))


class Station(Base):
    __tablename__ = "station"
    id = Column(INTEGER, primary_key=True)
    bureau = Column(String(20))
    state = Column(INTEGER)
    name = Column(String(20))
    address = Column(String(20))
    passenger = Column(Boolean)
    puggage = Column(Boolean)
    package = Column(Boolean)
