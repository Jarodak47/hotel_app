from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from core import dependencies
from core.config import settings
from utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.Stock])
def read_stock(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    stock = crud.stock.get_multi(db, skip=skip, limit=limit)
    return stock

@router.get("/", response_model=List[schemas.Stock])
def read_stock_by_statut(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    est_disponible : bool = None,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Retrieve room.
    """
    stock = crud.stock.get_by_est_disponible(db,est_libre)
    stock = crud.stock.get_multi(db, skip=skip, limit=limit)
    return stock

@router.post("/", response_model=schemas.Stock)
def create_stock(
    *,
    db: Session = Depends(dependencies.get_db),
    stock_in: schemas.StockCreate,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Add a new product in stock.
    """
    stock = crud.stock.get_by_title(db, title=stock_in.title)
    if stock:
        raise HTTPException(
            status_code=400,
            detail="The prduct with this title already exists in the system.",
        )
    stock = crud.stock.create(db, obj_in = stock_in)
    return stock


@router.get("/{stock_id}", response_model=schemas.Stock)
def read_stock_by_id(
    stock_id: int,
    current_user: models.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db),
) -> Any:
    """
    Get a specific chambre by id.
    """
    stock = crud.stock.get(db, id=stock_id)
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges to create rooms"
        )
    return stock


@router.put("/{stock_id}", response_model=schemas.Stock)
def update_stock(
    *,
    db: Session = Depends(dependencies.get_db),
    stock_id: int,
    stock_in: schemas.StockUpdate,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Update a room.
    """
    stock = crud.stock.get(db, id=stock_id)
    if not chambre:
        raise HTTPException(
            status_code=404,
            detail="The product with this id does not exist in stock",
        )
    stock = crud.stock.update(db, db_obj=stock, obj_in=stock_in)
    return stock
