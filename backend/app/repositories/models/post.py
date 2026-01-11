from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String

from .. import db
from .post_favorite import post_favorites_table
from .post_like import post_likes_table

if TYPE_CHECKING:
    from . import Board, Reply, User


class Post(db.Model):
    __tablename__ = 'posts'

    uuid: Mapped[UUID] = mapped_column(String(36), primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str]
    edit_count: Mapped[int] = mapped_column(default=0)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    created_time: Mapped[datetime]
    pin_weight: Mapped[int] = mapped_column(default=0)
    author_username: Mapped[str] = mapped_column(ForeignKey('users.username'))
    board_name: Mapped[str] = mapped_column(ForeignKey('boards.name'))

    author: Mapped['User'] = relationship(back_populates='posts')
    board: Mapped['Board'] = relationship(back_populates='posts')
    replies: Mapped[list['Reply']] = relationship(back_populates='post')
    users_liking: Mapped[list['User']] = relationship(
        secondary=post_likes_table, back_populates='posts_likes'
    )
    users_favoriting: Mapped[list['User']] = relationship(
        secondary=post_favorites_table, back_populates='posts_favorites'
    )

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'title': self.title,
            'content': self.content,
            'edit_count': self.edit_count,
            'is_deleted': self.is_deleted,
            'created_time': self.created_time.strftime("%Y/%m/%d"),
            'pin_weight': self.pin_weight,
            'author_username': self.author_username,
            'board_name': self.board_name,
            'like':len(self.users_liking),
        }