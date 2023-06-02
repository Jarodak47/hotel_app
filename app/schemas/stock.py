from typing import Optional,List
from enum import Enum
from pydantic import BaseModel


types_de_produits = ("A", "B", "C", "D", "E")
class TypeDeProduit(str, Enum):
    simple = "simple"
    double = "double"
    suite = "suite"

# Shared properties
class StockBase(BaseModel):
    code_stock: Optional[str] = None
    est_disponible: Optional[bool] = True
    description: Optional[str] = None
    unit_price: Optional[float] = 100
    type_de_produit: Optional[str] = None # Utiliser le type Enum de Python ici 



# Properties to receive via API on creation
class StockCreate(StockBase):
    code_stock : str



# Properties to receive via API on update
class StockUpdate(StockBase):
    unit_price : Optional[float] = 100


class StockInDBBase(StockBase):
    id: Optional[int] = None


    class Config:
        orm_mode = True


# Additional properties to return via API
class Stock(StockInDBBase):
    pass


# Additional properties stored in DB
class StockInDB(StockInDBBase):
    pass
    