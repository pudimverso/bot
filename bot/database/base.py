from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
)


class Base(MappedAsDataclass, DeclarativeBase):
    """
    Base class for SQLAlchemy database models.
    """

    __abstract__ = True
    __dataclass_params__ = {
        "frozen": True,
    }
