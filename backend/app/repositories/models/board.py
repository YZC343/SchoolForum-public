import this
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String

from .. import db
from .board_moderator import board_moderators_table

if TYPE_CHECKING:
    from . import Post, User


class Board(db.Model):
    __tablename__ = 'boards'

    name: Mapped[str] = mapped_column(String(100), primary_key=True)
    content: Mapped[str | None]

    posts: Mapped[list['Post']] = relationship(back_populates='board')
    moderator: Mapped[list['User']] = relationship(
        secondary=board_moderators_table, back_populates='boards_managing'
    )
    def to_dict(self):
        return {
            "name":self.name,
            "content":self.content,
        }