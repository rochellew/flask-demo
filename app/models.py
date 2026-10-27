from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from typing import TYPE_CHECKING
from .extensions import db

# Pyright can't see that db.Model is built from our Base, so point it at Base directly
if TYPE_CHECKING:
    from .extensions import Base as Model
else:
    Model = db.Model

class User(UserMixin, Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(150), unique=True)
    password_hash: Mapped[str] = mapped_column(String(150))
    is_admin: Mapped[bool] = mapped_column(default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)