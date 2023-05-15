from typing import TYPE_CHECKING
from sqlalchemy.sql import func

from sqlalchemy import Boolean,DateTime, Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Facture(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    invoice_id = Column(Integer, index=True)    
    is_complete = Column(Boolean(), default=False)
    #items = relationship("Item", back_populates="owner")
    created_date = Column(DateTime(timezone=True), server_default=func.now())
