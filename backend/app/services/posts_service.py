import uuid
from datetime import datetime

from sqlalchemy import and_, delete, insert, select
from sqlalchemy.sql import func

from ..repositories import db
from ..repositories.models import Post
from ..repositories.models.post_favorite import post_favorites_table
from ..repositories.models.post_like import post_likes_table


def publish_post(
    title: str, content: str, author_username: str, board_name: str
) -> bool:
    if not (title and content and board_name):
        return False

    db.session.add(
        Post(
            uuid=uuid.uuid4(),
            title=title,
            content=content,
            board_name=board_name,
            author_username=author_username,
            created_time=datetime.now(),
        )
    )
    db.session.commit()

    return True


def edit_post(uuid: uuid.UUID, title: str, content: str, board_name: str) -> bool:
    post: Post | None = db.session.execute(
        select(Post).where(Post.uuid == uuid)
    ).scalar_one_or_none()

    if post is None:
        return False

    post.title = title
    post.content = content
    post.board_name = board_name
    post.edit_count += 1

    db.session.commit()

    return True


def delete_post(post_uuid: uuid.UUID) -> bool:
    post: Post | None = db.session.execute(
        select(Post).where(Post.uuid == uuid)
    ).scalar_one_or_none()

    if Post is None:
        return False

    post.is_deleted = True
    db.session.commit()

    return True


def pin_post(post_uuid: uuid.UUID, weight: int) -> bool:
    post: Post | None = db.session.execute(
        select(Post).where(Post.uuid == uuid)
    ).scalar_one_or_none()

    if post is None:
        return False

    post.pin_weight = weight
    db.session.commit()

    return True


def like_post(post_uuid: uuid.UUID, username: str) -> bool:
    post: Post | None = db.session.execute(
        select(Post).where(Post.uuid == uuid)
    ).scalar_one_or_none()

    if post is None:
        return False

    if (
        db.session.execute(
            select(func.count(post_likes_table)).where(
                and_(
                    post_likes_table.c.username == username,
                    post_likes_table.c.post_uuid == post_uuid,
                )
            )
        ).scalar()
        == 0
    ):
        db.session.execute(
            insert(post_likes_table).values(username=username, post_uuid=post_uuid)
        )
    else:
        db.session.execute(
            delete(post_likes_table).where(
                and_(
                    post_likes_table.c.username == username,
                    post_likes_table.c.post_uuid == post_uuid,
                )
            )
        )

    db.commit()

    return True


def collect_post(post_uuid: uuid.UUID, username: str) -> bool:
    post: Post | None = db.session.execute(
        select(Post).where(Post.uuid == uuid)
    ).scalar_one_or_none()

    if post is None:
        return False

    if (
        db.session.execute(
            select(func.count(post_favorites_table)).where(
                and_(
                    post_likes_table.c.username == username,
                    post_likes_table.c.post_uuid == post_uuid,
                )
            )
        ).scalar()
        == 0
    ):
        db.session.execute(
            insert(post_favorites_table).values(username=username, post_uuid=post_uuid)
        )
    else:
        db.session.execute(
            delete(post_favorites_table).where(
                and_(
                    post_likes_table.c.username == username,
                    post_likes_table.c.post_uuid == post_uuid,
                )
            )
        )

    db.commit()

    return True


def is_author(username: str, post_uuid: uuid.UUID) -> bool:
    return (
        db.session.execute(select(Post).where(Post.uuid == post_uuid))
        .scalar_one()
        .author_username
        == username
    )
