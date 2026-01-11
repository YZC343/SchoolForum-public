import uuid

from sqlalchemy import and_, select

from ..repositories import db
from ..repositories.models import Reply


def delete_reply(post_uuid: uuid.UUID, sequence_no: int) -> bool:
    reply: Reply | None = db.session.execute(
        select(Reply).where(
            and_(Reply.post_uuid == post_uuid, Reply.sequence_no == sequence_no)
        )
    ).scalar_one_or_none()

    if reply is None:
        return False

    reply.is_deleted = True
    db.session.commit()

    return True


def is_author(username: str, post_uuid: uuid.UUID, sequence_no: int) -> bool:
    reply: Reply | None = db.session.execute(
        select(Reply).where(
            and_(Reply.post_uuid == post_uuid, Reply.sequence_no == sequence_no)
        )
    ).scalar_one_or_none()

    if reply is None:
        return False

    return reply.author_username == username
