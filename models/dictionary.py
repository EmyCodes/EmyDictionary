#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, Text
from resources import Base

class DictionaryModel(Base):
    """To be Updated"""
    __tablename__ = "dictionary"
    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String(80), nullable=False)
    meanings = Column(Text)
