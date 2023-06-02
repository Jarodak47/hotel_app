from typing import Optional,List
from pydantic import BaseModel
from enum import Enum


# Définir un enum pour les types de chambre
class TypeDeChambre(str, Enum):
    simple = "simple"
    double = "double"
    suite = "suite"

types_de_chambre = ("standard", "superieure", "deluxe", "suite", "familliale")


# Shared properties
class ChambreBase(BaseModel):
    code_chambre: Optional[str] = None
    est_libre: Optional[bool] = True
    description: Optional[str] = None
    type_de_chambre: Optional[str] = None # Utiliser le type Enum de Python ici 
    unit_price : Optional[float] = 100


# Properties to receive via API on creation
class ChambreCreate(ChambreBase):
    code_chambre : str


# Properties to receive via API on update
class ChambreUpdate(ChambreBase):
    pass


class ChambreInDBBase(ChambreBase):
    id: Optional[int] = None
    

    class Config:
        orm_mode = True


# Additional properties to return via API
class Chambre(ChambreInDBBase):
    pass


# Additional properties stored in DB
class ChambreInDB(ChambreInDBBase):
    pass
    