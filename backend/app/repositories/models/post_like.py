from sqlalchemy import Column, ForeignKey, Table

from .. import db

post_likes_table = Table(
    'post_likes',
    db.metadata,
    Column('username', ForeignKey('users.username'), primary_key=True),
    Column('post_uuid', ForeignKey('posts.uuid'), primary_key=True),
)