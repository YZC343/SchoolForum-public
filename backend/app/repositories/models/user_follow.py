from sqlalchemy import Column, ForeignKey, Table

from .. import db

user_follows_table = Table(
    'user_follows',
    db.metadata,
    Column('follower_username', ForeignKey('users.username'), primary_key=True),
    Column('followed_username', ForeignKey('users.username'), primary_key=True),
)