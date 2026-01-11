from datetime import datetime
from typing import Any

from sqlalchemy import and_, func, or_, select

from ..repositories import db
from ..repositories.models import PrivateMessage, User
from ..utils import Result


def send_message(sender_username: str, receiver_username: str, content: str) -> bool:
    if (
        db.session.execute(
            select(func.count(User)).where(
                or_(
                    User.username == sender_username, User.username == receiver_username
                )
            )
        ).scalar()
        != 2
    ):
        return False

    db.session.add(
        PrivateMessage(
            sender_username=sender_username,
            receiver_username=receiver_username,
            send_time=datetime.now(),
            content=content,
        )
    )

    return True


def query_message(username1: str, username2: str) -> Result[list[dict[str, Any]], str]:
    if (
        db.session.execute(
            select(func.count(User)).where(
                or_(User.username == username1, User.username == username2)
            )
        ).scalar()
        != 2
    ):
        return Result.err('Both users must exist.')

    return Result.ok(
        [
            msg.to_dict()
            for msg in db.session.execute(
                select(PrivateMessage)
                .where(
                    or_(
                        and_(
                            PrivateMessage.sender_username == username1,
                            PrivateMessage.receiver_username == username2,
                        ),
                        and_(
                            PrivateMessage.sender_username == username2,
                            PrivateMessage.receiver_username == username1,
                        ),
                    )
                )
                .order_by(PrivateMessage.send_time.desc())
            ).scalars()
        ]
    )
