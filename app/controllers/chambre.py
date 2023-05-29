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
    Retrieve room.
    """
    chambres = crud.chambre.get_multi(db, skip=skip, limit=limit)
    return chambres

@router.get("/by-statut{bool}", response_model=List[schemas.Chambre])
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
    return chambres


@router.get("/by-type{str}", response_model=List[schemas.Chambre])
def read_chambres_by_type(
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    type_de_chambre : str = None,
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Retrieve room.
    """
    chambres = crud.chambre.get_by_type(db,type_de_chambre)
    return chambres


@router.get("/by-code_chambre{str}", response_model=schemas.Chambre)
def read_chambre_by_code_(
    code_chambre : str ,
    db: Session = Depends(dependencies.get_db),
    current_user: models.User = Depends(dependencies.get_current_active_superuser),
) -> Any:
    """
    Retrieve room.
    """
    chambre = crud.chambre.get_by_code(db,code_chambre=code_chambre)
    if not chambre:
        raise HTTPException(
            status_code=404, detail="This room code doesn't exists in the system"
        )
    return chambre




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
    chambre = crud.chambre.get_by_code(db, code_chambre=chambre_in.code_chambre)
    if chambre:
        raise HTTPException(
            status_code=400,
            detail="The room with this code already exists in the system.",
        )
    chambre = crud.chambre.create(db, obj_in=chambre_in)
    return chambre


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
            status_code=404,detail="The room with this id does not exist in the system",
    )
    else:
        code_chambre = crud.chambre.get_by_code_chambre(db, code_chambre=chambre_in.code_chambre)
    if code_chambre and code_chambre.id != chambre_id:
        raise HTTPException(status_code=400,detail="This room code already exists in the system",
        )
    chambre = crud.chambre.update(db, db_obj=chambre, obj_in=chambre_in)
    return chambre



