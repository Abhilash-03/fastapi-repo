# what is dependency injection in fastapi?
# Dependency injection in FastAPI is a design pattern that allows you to manage and provide dependencies (such as services, database connections, or configurations) to your application components in a clean and efficient way. It helps to decouple (decouple means to separate or disconnect) the components of your application, making it easier to test, maintain, and scale.

from fastapi import FastAPI, Depends

app = FastAPI()

# def common_logic():
#     return {
#         "message": "This is a common logic that can be reused in multiple endpoints."
#     }

# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data

def get_current_user():
    return {"username": "John Doe", "role": "admin"}

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return {"message": f"Hello, {user['username']}! You are logged in as {user['role']}."}

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return {"message": f"Welcome to the dashboard, {user['username']}! Your role is {user['role']}."}