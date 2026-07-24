from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return {
        "user": "Authorized User",
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {
        "message" : "Secure data accessed",
        "user": user
    }