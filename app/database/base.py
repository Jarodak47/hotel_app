# Import all the models, so that Base has them before being
# imported by Alembic
from database.base_class import Base  # noqa
from models.item import Item  # noqa
from models.user import User  # noqa
from models.stock import Stock 
from models.chambre import Chambre  # noqa
 # noqa

