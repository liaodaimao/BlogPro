'''
  Flask插件
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # ORM
migrate = Migrate()  # 数据迁移


# 初始化插件
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app, db)

