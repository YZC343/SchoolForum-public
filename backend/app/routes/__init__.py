
from flask import Blueprint as _Blueprint

from . import auth as _auth
from . import board as _board
from . import message as _message
from . import posts as _posts
from . import replies as _replies
from . import user as _user
from . import user_info as _user_info

BP = _Blueprint('api', __name__)

BP.register_blueprint(_auth.BP, url_prefix='/auth')
BP.register_blueprint(_board.BP, url_prefix='/board')
BP.register_blueprint(_message.BP, url_prefix='/message')
BP.register_blueprint(_posts.BP, url_prefix='/posts')
BP.register_blueprint(_replies.BP, url_prefix='/replies')
BP.register_blueprint(_user.BP, url_prefix='/user')
BP.register_blueprint(_user_info.BP, url_prefix='/user_info')

__all__: list[str] = ['BP']
