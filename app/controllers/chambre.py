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


@router.get("/", response_model=List[schemas.Chambre])
def read_chambres(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    chambres = crud.chambre.get_multi(db, skip=skip, limit=limit)
    return chambres

@router.get("/", response_model=List[schemas.Chambre])
def read_chambres_by_statut(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    est_libre : bool = None,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Retrieve room.
    """
    chambres = crud.chambre.get_by_est_libre(db,est_libre)
    chambres = crud.chambre.get_multi(db, skip=skip, limit=limit)
    return chambres

@router.post("/", response_model=schemas.Chambre)
def create_chambre(
    *,
    db: Session = Depends(dependencies.get_db),
    chambre_in: schemas.ChambreCreate,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Create new chambre.
    """
    chambre = crud.chambre.get_by_numero(db, numero_de_chambre=chambre_in.numero_de_chambre)
    if chambre:
        raise HTTPException(
            status_code=400,
            detail="The room with this numero already exists in the system.",
        )
    chambre = crud.chambre.create(db, obj_in=chambre_in)
    return user


@router.get("/{chambre_id}", response_model=schemas.Chambre)
def read_chambre_by_id(
    chambre_id: int,
    current_user: models.User = Depends(dependencies.get_current_active_user),
    db: Session = Depends(dependencies.get_db),
) -> Any:
    """
    Get a specific chambre by id.
    """
    chambre = crud.chambre.get(db, id=chambre_id)
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges to create rooms"
        )
    return chambre


@router.put("/{chambre_id}", response_model=schemas.Chambre)
def update_chambre(
    *,
    db: Session = Depends(dependencies.get_db),
    chambre_id: int,
    chambre_in: schemas.ChambreUpdate,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Update a room.
    """
    chambre = crud.chambre.get(db, id=chambre_id)
    if not chambre:
        raise HTTPException(
            status_code=404,
            detail="The room with this id does not exist in the system",
        )
    chambre = crud.chambre.update(db, db_obj=chambre, obj_in=chambre_in)
    return chambre
