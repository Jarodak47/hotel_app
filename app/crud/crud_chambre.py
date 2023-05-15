from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.chambre import Chambre
from schemas.chambre import ChambreCreate, ChambreUpdate


class CRUDChambre(CRUDBase[Chambre, ChambreCreate, ChambreUpdate]):

    def get_by_numero(self, db: Session, *, numero_de_chambre: int) -> Optional[Chambre]:
        return db.query(Chambre).filter(Chambre.numero_de_chambre == numero_de_chambre).first()
    
    def get_by_est_libre(self, db: Session, *, bool: None) -> Optional[Chambre]:
        return db.query(Chambre).filter(Chambre.est_libre == est_libre).all()

    def create(self, db: Session, *, obj_in: ChambreCreate) -> Chambre:
        db_obj = Chambre(
            numero_de_chambre=obj_in.numero_de_chambre,
            est_libre=obj_in.est_libre,
            description=obj_in.description,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Chambre, obj_in: Union[ChambreUpdate, Dict[str, Any]]
    ) -> Chambre:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)


    def est_libre(self, user: Chambre) -> bool:
        return chambre.est_libre(Chambre)

chambre = CRUDChambre(Chambre)
