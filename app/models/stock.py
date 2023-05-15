from typing import TYPE_CHECKING
from sqlalchemy.sql import func

from sqlalchemy import Boolean,DateTime, Column, Integer, String
from sqlalchemy.orm import relationship

from database.base_class  import  Base


class Stock(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True,unique= True, default = None)
    description = Column(String,index=True, default = None)
    est_disponible = Column(Boolean, default=True)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())

