from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from typing import ClassVar
from flask_sqlalchemy.query import Query
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    query: ClassVar[Query]  # added by Flask-SQLAlchemy at runtime

db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
