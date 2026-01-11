from typing import Any

from sqlalchemy import select

from ..repositories import db
from ..repositories.models import User
from ..utils import Result


def pick_user_info(username: str) -> Result[dict[str, Any], str]:
    user: User | None = db.session.execute(
        select(User).where(User.username == username)
    ).scalar_one_or_none()

    if user is None:
        return Result.err('User must exist.')

    return Result.ok(user.to_dict())


def modify_user_info(
    username: str,
    *,
    nickname: str | None = None,
    avatar: str | None = None,
    signature: str | None = None,
) -> bool:
    user: User | None = db.session.execute(
        select(User).where(User.username == username)
    ).scalar_one_or_none()

    if user is None:
        return False

    if nickname is not None:
        user.nickname = nickname

    if avatar is not None:
        user.avatar = avatar

    if signature is not None:
        user.signature = signature

    db.session.commit()

    return True
