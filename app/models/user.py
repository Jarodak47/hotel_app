from typing import TYPE_CHECKING
from sqlalchemy.sql import func

from sqlalchemy import Boolean,DateTime, Column, Integer, String
from sqlalchemy.orm import relationship

from database.base_class  import  Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    last_connexion_date = Column(DateTime(timezone=True), onupdate=func.now())

