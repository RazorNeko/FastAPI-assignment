from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, UserDB
from database import TaskDB
from models import User, Task, UserWithTasks
from sqlalchemy import select
from sqlalchemy.orm import joinedload

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoint to create a new user
@app.post("/users/", response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)):
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# API endpoint to get a user by username
@app.get("/users/{username}", response_model=UserWithTasks)
async def read_user(username: str, db: Session = Depends(get_db)):
    query = select(UserDB).options(joinedload(UserDB.tasks)).filter(UserDB.username == username)
    user = db.execute(query).scalar()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# API endpoint to create a new task for a user
@app.post("/users/{username}/tasks/", response_model=Task)
async def create_task(username: str, task: Task, db: Session = Depends(get_db)):
    query = select(UserDB).filter(UserDB.username == username)
    user = db.execute(query).scalar()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_task = TaskDB(**task.dict(), user_id=user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

print("I am here I feel you!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)


