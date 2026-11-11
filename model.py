from pydantic import BaseModel,Field, EmailStr 
class User(BaseModel): 
       id : int = Field(...)
       title : str = Field(...,min_length=3,max_length=50) 
       email : EmailStr = Field(...)
       content : str = Field(...,min_length=3,max_length=50) 


       class Config: 
           schema_extra = {
               "example": {
                   "id": 1,
                   "title": "This is a title",
                   "email": "user@example.com",
                   "content": "This is the content"
               }
           }