from pydantic import BaseModel
from typing import Optional,List

class UserBase(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str
    class Config():
        orm_mode = True

class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int

class Blog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    id: int
    email: str
    blogs: List[Blog]
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    author: User
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str