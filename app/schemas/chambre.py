from typing import Optional

from pydantic import BaseModel


# Shared properties
class ChambreBase(BaseModel):
    numero_de_chambre: Optional[int] = None
    est_libre: Optional[bool] = True
    description: Optional[str] = None


# Properties to receive via API on creation
class ChambreCreate(ChambreBase):
    pass


# Properties to receive via API on update
class ChambreUpdate(ChambreBase):
    pass


class ChambreInDBBase(ChambreBase):
    id: Optional[int] = None
    created_date: str = None
    last_update_date: str = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Chambre(ChambreInDBBase):
    pass


# Additional properties stored in DB
class ChambreInDB(ChambreInDBBase):
    pass
    