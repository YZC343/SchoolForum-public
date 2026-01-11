from typing import Any

from sqlalchemy import select

from ..repositories import db
from ..repositories.models import Board


def add_board(name: str, content: str) -> bool:
    if (
        db.session.execute(select(Board).where(Board.name == name)).one_or_none()
        is None
    ):
        db.session.add(Board(name=name, content=content))
        db.session.commit()

        return True
    else:
        return False


def list_board() -> tuple[dict[str, Any]]:
    return tuple(b.to_dict() for b in db.session.execute(select(Board)).scalars())


def is_existing(board_name: str) -> bool:
    return (
        db.session.execute(select(Board).where(Board.name == board_name)).one_or_none()
        is not None
    )
