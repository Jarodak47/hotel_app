from typing import TYPE_CHECKING
from sqlalchemy.sql import func

from sqlalchemy import Boolean,DateTime, Column, Integer, String,Float,Enum
from sqlalchemy.orm import relationship

from database.base_class  import  Base

types_de_produits = ("simple", "double", "suite")


class Stock(Base):
    id = Column(Integer, primary_key=True, index=True)
    code_stock = Column(String,index=True,unique= True, default = None,nullable=False)
    description = Column(String,index=True,nullable=True)
    est_disponible = Column(Boolean, default=True)
    type_de_produit = Column(Enum(*types_de_produits, name="type_de_produit"), index=True,nullable=False)
    unit_price = Column(Float,index=True, default = 100, nullable = False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    last_update_date = Column(DateTime(timezone=True), onupdate=func.now())
    
