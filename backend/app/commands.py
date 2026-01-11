import click

from repositories import db


@click.command
def init_db_command():
    db.create_all()
