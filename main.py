
# Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional,List
import json
# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# Import libraries from FastAPI.
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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
        )
    last_name:str=Field(
       ...,
       min_length=1,
       max_length=50,
       )
    birth_day:Optional[date]=Field(default=None)

class userRegister(User):
    password:str=Field(
        ...,
        min_length=8,
        max_length=64,
        )

class Tweet(BaseModel):
    tweet_id:UUID=Field(...)
    content:str=Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at:datetime=Field(default=datetime.now())
    updated_at:Optional[datetime]=Field(default=None)
    by:User=Field(...)

# path operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}

## path Operations Users. Sign up a User
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register User",
    tags=["Users"]
)
def sigup(user:userRegister=Body(...)):
    """
    Sign  Up a User

    This path operation register a user in a app

    Parameters:
        - Request body parameters
           -user:UserRegister
    
    Returns a json with the basic user information:
        - user_id_UUID
        - Email: Emailstr
        - first_name:str
        - last_name:str
        - birth_date:data
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results=json.loads(f.read())
        user_dict=user.dict()
        user_dict["user_id"]=str(user_dict["user_id"])
        user_dict["birth_day"]=str(user_dict["birth_day"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


# # Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def sigup():
    pass

# # Show all Users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def showAllUsers():
    """
    Show all user on the app

    Parameters:
        
    Retunr A list of user on the app:
        - user_id_UUID
        - Email: Emailstr
        - first_name:str
        - last_name:str
        - birth_date:data
    """
    with open("users.json", "r", encoding="utf-8") as f:
        result=json.loads(f.read())
        return result

# #Shw one user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user by id on url",
    tags=["Users"]
)
def showOneUser():
    pass

# # Delete one user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def deleteOneUser():
    pass

# # Update an User
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update an User",
    tags=["Users"]
)
def UpdateOneUser():
    pass

## path Operations Tweets
#show all Tweets
@app.get(
    path="/showAll",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def showAllTweets():
    """
    Show all Tweets published by users

    Parameters: None
        
    Returns a json with the basic tweet information:

        - tweet_id:UUID
        - content:str
        - created_at:datetime
        - updated_at:Optional[datetime]
        - by:User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        result=json.loads(f.read())
        return result


# # post a Tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Post a Tweet tweets",
    tags=["Tweets"]
)
def postTweet(tweet:Tweet=Body(...)):
    """
    Post a Tweet

    This path operation post  a Tweet in the aplications

    Parameters:

        - Request body parameters
           -tweet:Tweet
    
    Returns a json with the basic tweet information:

        - tweet_id:UUID
        - content:str
        - created_at:datetime
        - updated_at:Optional[datetime]
        - by:User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results=json.loads(f.read())
        tweet_dict=tweet.dict()
        tweet_dict["tweet_id"]=str(tweet_dict["tweet_id"])
        tweet_dict["created_at"]=str(tweet_dict["created_at"])
        tweet_dict["updated_at"]=str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"]=str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_day"]=str(tweet_dict["by"]["birth_day"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

# # Show a Tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def showTweet():
    pass

# # delete a Tweet
@app.delete(
    path="/tweets/{user_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def deleteOneTweet():
    pass

# # Update a Tweet
@app.put(
    path="/tweets/{user_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweer",
    tags=["Tweets"]
)
def UpdateOneTweet():
    pass