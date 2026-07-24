from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundError(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundError)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "status_text": "Error",
            "message": f"User '{exc.name}' not found."
            },
    )

@app.get("/user/{name}")
def get_user(name: str):
    if name != "John Doe":
        raise UserNotFoundError(name)
    return {"name": "John Doe", "age": 30}