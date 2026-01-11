from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import db

if TYPE_CHECKING:
    from . import Post, User


class Reply(db.Model):
    __tablename__ = 'replies'

    sequence_no: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str]
    is_deleted: Mapped[bool] = mapped_column(default=False)
    created_time: Mapped[datetime]
    author_username: Mapped[str] = mapped_column(ForeignKey('users.username'))
    post_uuid: Mapped[UUID] = mapped_column(ForeignKey('posts.uuid'), primary_key=True)

    author: Mapped['User'] = relationship(back_populates='replies')
    post: Mapped['Post'] = relationship(back_populates='replies')

    def to_dict(self):
        return {
        "sequence_no":self.sequence_no,
        "content":self.content,
        "is_deleted":self.is_deleted,
        "created_time":self.created_time.strftime("%Y/%m/%d"),
        "author_username":self.author_username,
        "post_uuid":self.post_uuid,
        "author":self.author.to_dict(),
        "post":self.post.to_dict(),
    }
