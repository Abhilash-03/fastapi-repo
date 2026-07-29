from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

app = FastAPI()

class TodoList(BaseModel):
    title: str
    completed: bool = False

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Define a model for the "todos" table
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos")
def create_todo(todo: TodoList, db: Session = Depends(get_db)):
    todo = Todo(title=todo.title, completed=todo.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo created successfully",
        "todo": todo
    }   

# Read all data from the database
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "message": "Todos retrieved successfully",
        "total": len(todos),
        "data": todos
    }

# Read a single data from the database
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code= 404, detail="Todo not found")

    return {
        "message": "Todo retrieved successfully",
        "data": todo
    }

# Update a single data in the database
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoList, db: Session = Depends(get_db)):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    existing_todo.title = todo.title
    existing_todo.completed = todo.completed
    db.commit()
    db.refresh(existing_todo)

    return {
        "message": "Todo updated successfully",
        "data": existing_todo
    }

# Delete a single data from the database
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(existing_todo)
    db.commit()

    return {
        "message": "Todo deleted successfully",
        "data": existing_todo
    }