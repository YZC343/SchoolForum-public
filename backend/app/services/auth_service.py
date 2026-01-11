from datetime import datetime

from sqlalchemy import and_, select

from ..repositories import db
from ..repositories.models import User


def register(username: str, password: str) -> bool:
    if (
        db.session.execute(select(User).where(User.username == username)).one_or_none()
        is None
    ):
        db.session.add(
            User(
                username=username,
                nickname=username,
                password=password,
                signature='',
            )
        )
        db.session.commit()

        return True
    else:
        return False


def login(username: str, password: str) -> bool:
    return (
        db.session.execute(
            select(User).where(
                and_(
                    and_(User.username == username, User.password == password),
                    ~User.is_deleted,
                )
            )
        ).one_or_none()
        is not None
    )


def unregister(username: str, password: str) -> bool:
    user: User | None = db.session.execute(
        select(User).where(User.username == username and User.password == password)
    ).scalar_one_or_none()

    if user is not None:
        user.is_deleted = True
        db.session.commit()

        return True
    else:
        return False


def is_super_admin(username: str) -> bool:
    return (
        db.session.execute(select(User).where(User.username == username))
        .scalar_one()
        .is_super_admin
    )


def is_banned_user(username: str) -> bool:
    user: User = db.session.execute(
        select(User).where(User.username == username)
    ).scalar_one()

    if user.unban_date is None:
        return False

    if datetime.now() >= user.unban_date:
        user.unban_date = None
        db.session.commit()

        return False
    else:
        return True
