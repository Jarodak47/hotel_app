from sqlalchemy.orm import Session
import crud, schemas
from database.session import engine
from alembic.config import Config as AlembicConfig
from alembic import command as alembic_command
from core.config import settings
from database.base import Base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    #alembic_cfg = AlembicConfig("alembic.ini")
    #alembic_command.revision(alembic_cfg,autogenerate=True, message="new migration")
    #alembic_command.upgrade(alembic_cfg, "head")
    #alembic_command.stamp(alembic_cfg, "head")
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            phone_number=settings.FIRST_SUPERUSER_PHONE,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
