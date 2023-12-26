#!/usr/bin/python3
# from models.dictionary import DictionaryModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import username, password, host, database
from resources.interpreter import create_table

Base = declarative_base()

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")
metadata = MetaData()
Session = sessionmaker(bind=engine)

session = Session()

create_table(engine)



