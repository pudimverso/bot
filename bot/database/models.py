from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Literal, Optional, TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from bot.database.base import Base


class Member(Base):
    """Tabela de membros do servidor"""

    __tablename__ = "members"
    """Nome da tabela"""

    user_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    """ID do usuário"""
    user_name: Mapped[str] = mapped_column(nullable=False)
    """Nome do usuário"""
    user_nickname: Mapped[Optional[str]] = mapped_column(nullable=True)
    """Apelido do usuário"""
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    """Data de criação do registro"""
    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    """Data de entrada no servidor"""
