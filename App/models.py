from App.exts import db




# 分类    一个分类有多篇文章
class Classification(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    alias = db.Column(db.String(100))
    keyword = db.Column(db.String(100))
    parentnode = db.Column(db.String(100))
    describe = db.Column(db.Text)
    # 建立一个关系 是让2个模型建立关系，不会在数据库中创建字段的
    # 这里是反向关联，用分类中的属性联系到文章
    contents = db.relationship("Content", backref="my_classification", lazy="dynamic")


# 文章
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),unique=True)
    text = db.Column(db.Text)# 文本内容
    comment = db. Column(db.Integer,default=0)
    keyword = db.Column(db.String(50))
    describe = db.Column(db.Text)
    label = db.Column(db.String(50),default='无')
    img = db.Column(db.String(200))
    data = db.Column(db.DateTime)
    # 外键
    classification = db.Column(db.Integer, db.ForeignKey(Classification.id))


# 用户
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    passwd = db.Column(db.String(20))
    username = db.Column(db.String(20),unique=True)
    phone = db.Column(db.String(30))
