#!/usr/bin/env python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine=create_engine('sqlite:///recipes.db')
Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base() 