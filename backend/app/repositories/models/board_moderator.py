from sqlalchemy import Column, ForeignKey, Table

from .. import db

board_moderators_table = Table(
    'board_moderators',
    db.metadata,
    Column('moderator_username', ForeignKey('users.username'), primary_key=True),
    Column('board_name', ForeignKey('boards.name'), primary_key=True),
)