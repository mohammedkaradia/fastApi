from sqlalchemy import Table, Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index=True)
    firstname = Column(String(50), unique=False)
    lastname = Column(String(50), unique=False)
    email = Column(String(50), unique=True)
    phoneno = Column(String(10), unique=True)
