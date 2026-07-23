from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
what is pydantic model?
Pydantic is a data validation and settings management library for Python, which uses Python type annotations to define data models. A Pydantic model is a class that inherits from `BaseModel` and defines the structure of the data, including the types of each field. Pydantic automatically validates the data against the defined types and can also provide default values, custom validation, and serialization/deserialization of data.
"""
# nested model example:

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    email: str
    age: int
    address: Address

@app.post("/create_user")
async def create_user(user: User):
    return {
       "message": "User created successfully",
       "user": user
    }