from sqlalchemy import Column, ForeignKey, Table

from .. import db

post_favorites_table = Table(
    'post_favorites',
    db.metadata,
    Column('username', ForeignKey('users.username'), primary_key=True),
    Column('post_uuid', ForeignKey('posts.uuid'), primary_key=True),
)