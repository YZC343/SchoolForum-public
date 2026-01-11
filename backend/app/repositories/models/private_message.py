from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import db

if TYPE_CHECKING:
    from . import User


class PrivateMessage(db.Model):
    __tablename__ = 'private_messages'

    sender_username: Mapped[str] = mapped_column(
        ForeignKey('users.username'), primary_key=True
    )
    receiver_username: Mapped[str] = mapped_column(
        ForeignKey('users.username'), primary_key=True
    )
    send_time: Mapped[datetime] = mapped_column(primary_key=True)
    content: Mapped[str]

    sender: Mapped['User'] = relationship(
        foreign_keys=[sender_username], back_populates='messages_sended'
    )
    receiver: Mapped['User'] = relationship(
        foreign_keys=[receiver_username], back_populates='messages_received'
    )

    def to_dict(self):
        raise NotImplementedError