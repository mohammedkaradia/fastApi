from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector

connection = "mysql+mysqlconnector://root:password@mysql/test"

# connection = "mysql+mysqlconnector://root@localhost:3306/test" //locally through xamp

engine = create_engine(connection, pool_size= 10, max_overflow= 30)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = declarative_base()