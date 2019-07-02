from flask import Flask
from App.views import blue
from App.exts import init_exts


def create_app():
    app = Flask(__name__)

    # 配置数据库
    # mysql
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/blogpro'
    # 可视化连接时Pycharm2019，URL添加时区：
    #  jdbc:mysql://localhost:3306/flaskdb?serverTimezone=UTC
    app.config['SECRET_KEY']='123EFDFSDV'

    # 禁止‘追踪修改’
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 修改成开发环境
    app.config['ENV'] = 'development'

    # 注册蓝图
    app.register_blueprint(blue)

    # 初始化插件
    init_exts(app)

    return app

