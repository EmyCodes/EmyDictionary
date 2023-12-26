#!/usr/bin/python3
# from models import data
# from resources.interpreter import load_data_from_db
# from resources.base import session

#!/usr/bin/python3
# from models.dictionary import DictionaryModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import username, password, host, database
from resources.interpreter import create_table, load_data_from_db

Base = declarative_base()

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")
metadata = MetaData()
Session = sessionmaker(bind=engine)

session = Session()

create_table(engine)


special_commands = ["Cancel -f", "Terminate -f", "Exit -f", "Quit -f",
                    "Cancel -F", "Terminate -F", "Exit -F", "Quit -F"]

iterate = True
while iterate:
    user = input("Enter a word: ")
    if user.capitalize() in special_commands:
        iterate = False
    else:
        meanings = load_data_from_db(user, session)
        for meaning in meanings:
            print(f"\t{meaning} \n")
