from typing import Optional

from pydantic import BaseModel

# Shared properties
class StockBase(BaseModel):
    code_stock: Optional[str] = None
    est_disponible: Optional[bool] = True
    description: Optional[str] = None
    unit_price: Optional[float] = None
    stock_type: Optional[str] = None


# Properties to receive via API on creation
class StockCreate(StockBase):
    code_stock : str
    


# Properties to receive via API on update
class StockUpdate(StockBase):
    unit_price : Optional[float] = None


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
    