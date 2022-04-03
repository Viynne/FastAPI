from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    net_worth: Optional[int] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    net_worth: Optional[int] = None


list_of_users = []


@app.post('/new/', response_model=UserOut, response_model_exclude_defaults=True)
async def request_info(user: UserIn):
    list_of_users.append(user)
    return user


@app.get("/huh")
async def user():
    return {"Name": list_of_users[-1]}, len(list_of_users)
