from fastapi import FastAPI

app = FastAPI()

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
    
