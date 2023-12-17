from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

#DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_URL = "mysql+mysqlconnector://Top:!234Qwer@host.docker.internal/test"
#DATABASE_URL = "mysql+mysqlconnector://Top:@mysql/test"
#DATABASE_URL = "mysql+mysqlconnector://Top:!234Qwer@host.docker.internal/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))

    tasks = relationship("TaskDB", back_populates="user")

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    short_description = Column(String(50))
    detailed_description = Column(String(50))
    status = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("UserDB", back_populates="tasks")

Base.metadata.create_all(bind=engine)
