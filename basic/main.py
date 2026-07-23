from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/about")
def about():
    return {"message": "This is a About page."}

@app.get("/contact")
def contact():
    return {"message": "This is a Contact page."}

@app.get("/items/{itemId}")
def user_item(itemId: int):
    return {"item_id": itemId, "message": f"Details for item {itemId}."}

# Query parameters example
@app.get("/search")
def search(query: str = None):
    if query:
        return {"message": f"Search results for query: {query}"}
    else:
        return {"message": "No search query provided."}
    

# post route example
@app.post("/create-user")
def create_user(name: str, age: int):
    return {
        "name": name,
        "age": age,
    }
"""
To check the post route, you can go to /docs in the browser and test the create-user endpoint with query parameters. For example, you can use the following URL to test it:
Output:
Request URL
http://127.0.0.1:8000/create-user?name=Abhilash&age=24 -> when we fill the name and age parameters in the query string, it will return a JSON response with the provided name and age. and it changes the request url and add name and age parameters in the url.

but if we don't want to change the request url and expose the parameters in the request url, so we can do in this way:
"""

@app.post("/create-user-body")
def create_user_body(user: dict):
    return{
        "message": "User created!",
        "user": user,
    }

# here we don't need to expose the parameters in the request url, instead we can send the parameters in the request body as a JSON object. For example, you can use the following JSON object to test it: 

# {
#     "name": "Abhilash",
#     "age": 24
# }


# but,
# as we were mentioning the type of the parameters in the first post route, we couldn't able to mention the type of the parameters in the second post route, so we can use Pydantic models to define the request body and validate the data.

# here is the example of using Pydantic models to define the request body and validate the data:
"""
first: we've defined a Pydantic model called User with two fields: name and age. Then, we've used this model as the type of the user parameter in the create_user_pydantic function. FastAPI will automatically validate the request body against the User model and return a 422 Unprocessable Entity error if the data is invalid.

second: we've used the user parameter in the response to return the validated data. FastAPI will automatically convert the Pydantic model to a JSON object in the response.
"""
@app.post("/create-user-pydantic")
def create_user_pydantic(user: User):
    return {
        "message": "User created!",
        "user": user,
    }