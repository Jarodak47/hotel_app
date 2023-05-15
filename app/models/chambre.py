from typing import TYPE_CHECKING
from sqlalchemy.sql import func

from sqlalchemy import Boolean,DateTime, Column, Integer, String
from sqlalchemy.orm import relationship

from database.base_class  import  Base


class Chambre(Base):
    id = Column(Integer, primary_key=True, index=True)
    numero_de_chambre = Column(String, index=True)
    description = Column(String,index=True, default = None)
    est_libre = Column(Boolean(), default=True)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    last_update_date = Column(DateTime(timezone=True), onupdate=func.now())

