#!/usr/bin/python3
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import pymysql

Base = declarative_base()
metadata = Base.metadata

engine = create_engine('mysql+pymysql://root:root@47.105.137.19:3306/fmss')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

db_conn = pymysql.Connection(host='47.105.137.19',
                        port=3306,
                        user='root',
                        password='root',
                        db='fmss',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor )
