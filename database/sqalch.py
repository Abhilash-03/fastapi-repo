from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

# Establish a connection to the SQLite database (test.db) using SQLAlchemy.
engine = create_engine(
    DATABASE_URL,
    connect_args= {"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine) # Create a session factory that will be used to create new database sessions. The sessionLocal object is a factory for creating new Session objects, which are used to interact with the database.

Base = declarative_base() # Create a base class for the SQLAlchemy models. This base class will be used to define the structure of the database tables and their relationships.

# Define a model for the "todos" table
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine) # Create the tables in the database based on the defined models. This will create the "todos" table if it doesn't already exist.

# Dependency to get a database session for each request
def get_db():
    db = sessionLocal() # Create a new database session
    try:
        yield db # Yield the session to be used in the route handlers
    finally:
        db.close() # Close the session after the request is completed

@app.get('/')
def home(db: Session = Depends(get_db)):
    return {
        "message": "SQLAlchemy database connection established successfully!"
    }