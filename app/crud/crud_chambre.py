from typing import Any, Dict, Optional, Union,List

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.chambre import Chambre
from schemas.chambre import ChambreCreate, ChambreUpdate # Importer le type TypeDeChambre ici


class CRUDChambre(CRUDBase[Chambre, ChambreCreate, ChambreUpdate]):

    def get_by_code(self, db: Session,*,code_chambre : str = None ) -> Optional[Chambre]:
        return db.query(Chambre).filter(Chambre.code_chambre == code_chambre).first()

    def get_by_est_libre(self, db: Session, est_libre: bool) -> Optional[List[Chambre]]:
        return db.query(Chambre).filter(Chambre.est_libre == est_libre).all()
    
    """def get_by_type(self, db: Session,type_de_chambre: str) -> Optional[List[Chambre]]:
        return db.query(Chambre).filter(Chambre.type_de_chambre == type_de_chambre).all()"""

    def get_by_type(self, db: Session,*,type_de_chambre: Optional[List[str]]= None ) -> Optional[List[Chambre]]: 
        # Utiliser le type List[TypeDeChambre] ici
        return db.query(Chambre).filter(Chambre.type_de_chambre.in_(type_de_chambre)).all() # Utiliser la méthode in_ ici

    def create(self, db: Session, *, obj_in: ChambreCreate) -> Chambre:
        db_obj = Chambre(
            code_chambre = obj_in.code_chambre,
            type_de_chambre = obj_in.type_de_chambre,
            est_libre = obj_in.est_libre,
            description = obj_in.description,
            unit_price =  obj_in.unit_price,
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
        return Chambre.est_libre

chambre = CRUDChambre(Chambre)
