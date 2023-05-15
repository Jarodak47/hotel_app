from typing import Optional

from pydantic import BaseModel

# Shared properties
class StockBase(BaseModel):
    title: Optional[str] = None
    est_disponible: Optional[bool] = True
    description: Optional[str] = None


# Properties to receive via API on creation
class StockCreate(StockBase):
    pass


# Properties to receive via API on update
class StockUpdate(StockBase):
    pass


class StockInDBBase(StockBase):
    id: Optional[int] = None
    created_date : str = None
    updated_date: str = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Stock(StockInDBBase):
    pass


# Additional properties stored in DB
class StockInDB(StockInDBBase):
    pass
    