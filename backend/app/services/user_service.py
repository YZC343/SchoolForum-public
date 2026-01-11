from datetime import datetime

from sqlalchemy import and_, delete, func, insert, select

from ..repositories import db
from ..repositories.models import User
from ..repositories.models.user_follow import user_follows_table


def subscribe_user(follower_username: str, followee_username: str):
    if (
        db.session.execute(
            select(User).where(User.username == followee_username)
        ).scalar_one_or_none()
        is None
    ):
        return False

    if (
        db.session.execute(
            select(func.count(user_follows_table)).where(
                and_(
                    user_follows_table.c.follower_username == follower_username,
                    user_follows_table.c.followed_username == followee_username,
                )
            )
        ).scalar()
        == 0
    ):
        db.session.execute(
            insert(user_follows_table).values(
                follower_username=followee_username, followee_username=followee_username
            )
        )
    else:
        db.session.execute(
            delete(user_follows_table).where(
                and_(
                    user_follows_table.c.follower_username == follower_username,
                    user_follows_table.c.followed_username == followee_username,
                )
            )
        )

    db.commit()

    return True


def ban_user(username: str, dt: datetime) -> bool:
    user: User | None = db.session.execute(
        select(User).where(User.username == username)
    ).scalar_one_or_none()

    if user is None:
        return False

    user.unban_date = dt
    db.session.commit()

    return True
