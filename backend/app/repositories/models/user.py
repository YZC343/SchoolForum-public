from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String

from .. import db
from .board_moderator import board_moderators_table
from .post_favorite import post_favorites_table
from .post_like import post_likes_table
from .user_follow import user_follows_table

if TYPE_CHECKING:
    from . import Board, Post, PrivateMessage, Reply


class User(db.Model):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(50), primary_key=True)
    password: Mapped[str] = mapped_column(String(255))
    is_super_admin: Mapped[bool] = mapped_column(default=False)
    unban_date: Mapped[datetime | None]
    nickname: Mapped[str] = mapped_column(String(50))
    avatar: Mapped[str | None] = mapped_column(String(255))
    signature: Mapped[str]
    is_deleted: Mapped[bool] = mapped_column(default=False)

    posts: Mapped[list['Post']] = relationship(back_populates='author')
    replies: Mapped[list['Reply']] = relationship(back_populates='author')
    following_users: Mapped[list['User']] = relationship(
        secondary=user_follows_table,
        primaryjoin=username == user_follows_table.c.follower_username,
        secondaryjoin=username == user_follows_table.c.followed_username,
        back_populates='followed_users',
    )
    followed_users: Mapped[list['User']] = relationship(
        secondary=user_follows_table,
        primaryjoin=username == user_follows_table.c.followed_username,
        secondaryjoin=username == user_follows_table.c.follower_username,
        back_populates='following_users',
    )
    messages_sended: Mapped[list['PrivateMessage']] = relationship(
        primaryjoin='User.username == PrivateMessage.sender_username',
        back_populates='sender',
    )
    messages_received: Mapped[list['PrivateMessage']] = relationship(
        primaryjoin='User.username == PrivateMessage.receiver_username',
        back_populates='receiver',
    )
    boards_managing: Mapped[list['Board']] = relationship(
        secondary=board_moderators_table, back_populates='moderator'
    )
    posts_likes: Mapped[list['Post']] = relationship(
        secondary=post_likes_table, back_populates='users_liking'
    )
    posts_favorites: Mapped[list['Post']] = relationship(
        secondary=post_favorites_table, back_populates='users_favoriting'
    )

    def to_dict(self):
        return {
            'username': self.username,
            'nickname': self.nickname,
            'avatar': self.avatar,
            'signature': self.signature,
            'following_users': self.following_users,
            'is_super_admin': self.is_super_admin,
        }