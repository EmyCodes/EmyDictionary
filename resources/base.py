#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import username, password, host, database

Base = declarative_base()

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

Session = sessionmaker(bind=engine)

session = Session()

