from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind = engine)


class UserBase(BaseModel):
    #id: int
    firstname: str
    lastname: str
    email: str
    phoneno: str

class UserModel(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    phoneno: str

def get_db():
    db = Sessionlocal()
    try: 
        yield db

    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/users/", status_code= status.HTTP_200_OK)
async def read_user(db: db_dependency):
    return db.query(models.User).all()

@app.get("/users/{user_Id}", status_code= status.HTTP_200_OK)
async def read_user(user_Id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_Id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.put("/users/", status_code= status.HTTP_200_OK)
async def update_user(user: UserModel, db: db_dependency):
    db_user = db.query(models.User).get(user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    for field, value in user.dict(exclude_unset=True).items():
        setattr(db_user, field, value)
        
    db.commit()
    return db_user

@app.delete("/users/{user_Id}", status_code= status.HTTP_200_OK)
async def delete_post(user_Id: int, db: db_dependency):
    db_user = db.query(models.User).get(user_Id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    db.delete(db_user)
    db.commit()