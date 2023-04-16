import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
with open("private/db_connect.json") as db_connect_file:
    db_connect = json.load(db_connect_file)
USER = db_connect["user"]
PW = db_connect["password"]
HOST = db_connect["host"]
PORT = db_connect["port"]
DB_NAME = db_connect["db_name"]
SQLALCHEMY_DATABASE_URL = ("mysql+mysqlconnector://"
                           + f"{USER}:"
                           + f"{PW}@"
                           + f"{HOST}:"
                           + f"{PORT}/"
                           + f"{DB_NAME}?charset=utf8mb4")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()