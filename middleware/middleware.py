from fastapi import FastAPI, Request
from time import time

app = FastAPI()

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#     # Perform some logic before processing the request
#     print(f"Request URL: {request.url}")
    
#     # Call the next middleware or route handler
#     response = await call_next(request)
    
#     # Perform some logic after processing the request
#     print(f"Response status code: {response.status_code}")
    
#     return response

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# logging middleware example
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time()

    response = await call_next(request)

    process_time = time() - start_time

    print(f"Path: {request.url.path} | Time: {process_time:.4f} seconds | Status Code: {response.status_code}")

    return response
