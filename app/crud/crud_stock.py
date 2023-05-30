from typing import Any, Dict, Optional, Union,List

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.stock import Stock
from schemas.stock import StockCreate, StockUpdate


class CRUDStock(CRUDBase[Stock, StockCreate, StockUpdate]):
    
    def get_by_est_disponible(self, db: Session,est_disponible: bool) -> Optional[List[Stock]]:
        return db.query(Stock).filter(Stock.est_disponible == est_disponible).all()

    def get_by_type(self, db: Session,*,type_de_produit: Optional[List[str]]= None) -> Optional[List[Stock]]: 
        # Utiliser le type List[TypeDeChambre] ici
        return db.query(Chambre).filter(Chambre.type_de_chambre.in_(type_de_chambre)).all() # Utiliser la méthode in_ ici

    def get_by_code(self, db: Session,*,code_stock : str) -> Optional[Stock]:
        return db.query(Stock).filter(Stock.code_stock == code_stock).first()

    def create(self, db: Session, *, obj_in: StockCreate) -> Stock:
        db_obj = Stock(
            code_stock=obj_in.code_stock,
            est_disponible = obj_in.est_disponible,
            description=obj_in.description,
            type_de_produit = obj_in.type_de_produit,
            unit_price=obj_in.unit_price,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Stock, obj_in: Union[StockUpdate, Dict[str, Any]]
    ) -> Stock:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)
        
    
    def est_disponible(self, stock: Stock) -> bool:
        return stock.est_disponible

stock = CRUDStock(Stock)