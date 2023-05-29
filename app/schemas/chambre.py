from typing import Optional

from pydantic import BaseModel


# Shared properties
class ChambreBase(BaseModel):
    code_chambre: Optional[str] = None
    est_libre: Optional[bool] = True
    description: Optional[str] = None
    type_de_chambre: Optional[str] = None
    unit_price : Optional[float] = None


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
    