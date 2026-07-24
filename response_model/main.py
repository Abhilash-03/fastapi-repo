from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserResponse(BaseModel):
    name: str
    age: int

@app.get("/users", response_model=UserResponse)
def get_users():
    return {
        "name": "John Doe",
        "age": 30,
        "password": "secret123"
    }

# why we use response_model in FastAPI?
# In FastAPI, the `response_model` parameter is used to define the structure of the response that will be returned by an endpoint. It allows you to specify a Pydantic model that describes the expected output format, which provides several benefits:

# 1. **Data Validation**: By using a response model, FastAPI automatically validates the data being returned from the endpoint against the defined Pydantic model. This ensures that the response adheres to the expected structure and types, reducing the risk of returning invalid or unexpected data.

# 2. **Automatic Documentation**: FastAPI generates interactive API documentation (using Swagger UI and Redoc) based on the response models defined for each endpoint. This makes it easier for developers to understand the API's expected responses and how to interact with it.

# 3. **Data Filtering**: The response model allows you to filter out sensitive or unnecessary fields from the response. In the provided example, even though the endpoint returns a dictionary containing a password, the `response_model` ensures that only the `name` and `age` fields are included in the final response sent to the client. This helps in maintaining data privacy and security. 


# status code and custom response Example:

@app.post("/create_user", status_code= status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully"}

# http exception example:

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"name": "John Doe", "age": 30}

