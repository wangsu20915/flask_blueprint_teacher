from flask import*

# 定义蓝图
blue_app2 = Blueprint("blue_app2",__name__)

# 定义路由
@blue_app2.route("/apptwo")
def two():
    return "这是来自蓝图2页面"