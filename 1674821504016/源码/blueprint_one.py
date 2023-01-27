from flask import*

# 定义蓝图
blue_app1 = Blueprint("blue_app1",__name__)

# 定义路由
@blue_app1.route("/appone")
def one():
    return "这是来自蓝图1页面"