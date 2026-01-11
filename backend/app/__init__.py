# def create_app(test_config=None):
# # create and configure the app
# app = Flask(__name__, instance_relative_config=True)
# app.config.from_mapping(
# SECRET_KEY='dev',
# DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
# )
#
# if test_config is None:
# # load the instance config, if it exists, when not testing
# app.config.from_pyfile('config.py', silent=True)
# else:
# # load the test config if passed in
# app.config.from_mapping(test_config)
#
# # ensure the instance folder exists
# try:
# os.makedirs(app.instance_path)
# except OSError:
# pass
#
# # a simple page that says hello
# @app.route('/hello')
# def hello():
# return 'Hello, World!'
#
# return app
from flask import Flask
from flask_cors import CORS
import routes
from repositories import db

def create_app() -> Flask:
    app = Flask(__name__)
    #app.config.from_object(Config)

    # 数据库配置
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/schoolforum'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config['SECRET_KEY'] = 'your-secret-key-here'
    # 初始化数据库
    db.init_app(app)
    # 创建数据库表
    with app.app_context():
        db.create_all()

    app.secret_key = 'your_secret_key'
    CORS(app, supports_credentials=True, origins=['http://localhost:5173'])  # 允许来自前端地址的请求携

    app.register_blueprint(routes.BP, url_prefix='/api')

    return app

create_app().run(debug=True)
