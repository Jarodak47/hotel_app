from typing import Any, List,Optional

from fastapi import APIRouter, Body, Depends, HTTPException,Query,Body
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from schemas.stock import TypeDeProduit
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

@router.get("/by-disponibilite{est_disponible}", response_model=List[schemas.Stock])
def read_stock_by_disponibilite(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    est_disponible : bool = None,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
    ) -> Any:
    """
    Retrieve stock by availability.
    """
    stocks = crud.stock.get_by_est_disponible(db,est_disponible)
    return stocks

@router.post("/", response_model=schemas.Stock)
def create_stock(
    *,
    db: Session = Depends(dependencies.get_db),
    stock_in:schemas.StockCreate,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Add a new product in stock.
    """
    stock = crud.stock.get_by_code(db, code_stock=stock_in.code_stock)
    if stock:
        raise HTTPException(
            status_code=400,
            detail="The product with this code already exists in the system.",
        )
    stock = crud.stock.create(db, obj_in = stock_in)
    return stock


@router.get("/{stock_id:int}", response_model=schemas.Stock)
def read_stock_by_id(
    stock_id: int,
    current_user: models.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db),
) -> Any:
    """
    Get a specific product in stock by id.
    """
    stock = crud.stock.get(db, id=stock_id)
    if not stock:
        raise HTTPException(
            status_code=404, detail="This product  doesn't exists in stock"
        )
    return stock


@router.get("/{code_stock:str}", response_model=schemas.Stock)
def read_stock_by_code(
    # Déclarer le paramètre code_stock comme un paramètre de chemin de type str
    code_stock: str,
    # Utiliser les dépendances pour obtenir l'utilisateur courant et la session de base de données
    current_user: models.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db),
) -> Any:
    """
    Get a specific product in stock by code.
    """
    # Appeler la fonction get_by_code_stock avec le code_stock et la session de base de données
    stock = crud.stock.get_by_code(db,code_stock=code_stock)
    # Vérifier si le produit existe, sinon lever une exception HTTPException avec le status_code 404
    if not stock:
        raise HTTPException(
            status_code=404, detail="This product code doesn't exists in stock"
        )
    # Retourner le produit trouvé
    return stock

@router.get("/by-type", response_model=Optional[List[schemas.Stock]]) 
def read_stock_by_type(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    type_de_produit : Optional[List[TypeDeProduit]]= Query(None), # Mettre le paramètre type_de_chambre dans la requête
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
    ) -> Any:
    """
    Retrieve room.
    """
    stock = crud.stock.get_by_type(db,type_de_produit=type_de_produit)
    if not stock:
        raise HTTPException(
            status_code=404, detail="product's  of this(those) type doesn't exists in the system"
        )
    return stock


@router.put("/{stock_id:int}", response_model=schemas.Stock)
def update_stock(
    *,
    db: Session = Depends(dependencies.get_db),
    stock_id: int,
    stock_in: schemas.StockUpdate,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Update a product in stock.
    """
    stock = crud.stock.get(db, id=stock_id)    
    if not stock:
        raise HTTPException(
            status_code=404,
            detail="The product with this id does not exist in stock",
        )
    else:
        code_stock = crud.stock.get_by_code_stock(db, code_stock=stock_in.code_stock)
    if code_stock and code_stock.id != stock_id:
        raise HTTPException(status_code=400,detail="This product code already exists in the system",
        )
    stock = crud.stock.update(db, db_obj=stock, obj_in=stock_in)
    return stock
    

