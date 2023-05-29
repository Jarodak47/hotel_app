from typing import TYPE_CHECKING
from sqlalchemy.sql import func

from sqlalchemy import Boolean,DateTime, Column, Integer, String,Float
from sqlalchemy.orm import relationship

from database.base_class  import  Base


class Chambre(Base):
    id = Column(Integer, primary_key=True, index=True)
    code_chambre = Column(String, index=True,unique=True,default=None,nullable=False)
    type_de_chambre = Column(String, index=True,nullable=False)
    description = Column(String,index=True, default = None)
    unit_price = Column(Float,index=True, default = 100, nullable = False)
    est_libre = Column(Boolean(), default=True)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    last_update_date = Column(DateTime(timezone=True), onupdate=func.now())

