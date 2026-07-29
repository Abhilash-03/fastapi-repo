import requests
from fastapi import FastAPI

app = FastAPI()

# get posts from the JSONPlaceholder API
@app.get("/fetch-posts")
def fetch_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        return {
            "message": "Posts fetched successfully!",
            "total": len(posts),
            "data": posts
        }
    else:
        return {
            "message": "Failed to fetch posts",
            "status_code": response.status_code
        }

# get single post from the JSONPlaceholder API
@app.get("/fetch-posts/{post_id}")
def fetch_single_post(post_id: int):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        post = response.json()
        return {
            "message": "Post fetched successfully!",
            "data": post
        }
    else:
        return {
            "message": "Failed to fetch post",
            "status_code": response.status_code
        }
