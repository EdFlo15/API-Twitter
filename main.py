
# Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional,List
# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# Import libraries from FastAPI.
from fastapi import FastAPI
from fastapi import status


app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id:UUID=Field(...)
    email:EmailStr=Field(...)

class UserLogin(UserBase):
    password:str=Field(
        ...,
        min_length=8,
        max_length=64,

        )
class User(UserBase):
    first_name:str=Field(
        ...,
        min_length=1,
        max_length=50,
        ),
    last_name:str=Field(
       ...,
       min_length=1,
       max_length=50,
       ),
    birth_day:Optional[date]=Field(default=None)

class Tweet(BaseModel):
    tweet_id:UUID=Field(...)
    content:str=Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at:datetime=Field(default=datetime.now)
    updated_at:Optional[datetime]=Field(default=None)
    by:User=Field(...)

# path operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}

## Users
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register User",
    tags=["Users"]
)
def sigup():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def sigup():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def shorAllUsers():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user by id on url",
    tags=["Users"]
)
def showOneUser():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def deleteUser():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update an User",
    tags=["Users"]
)
def UpdateOneUser():
    pass
