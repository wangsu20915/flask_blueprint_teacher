from flask import *          # 不建议这么做，我有点懒，请见谅

# 引入蓝图
from blueprint_one import blue_app1         # 建议只引入Blueprint对象，如左侧
from blueprint_two import blue_app2         # 建议只引入Blueprint对象，如左侧

# 先定义Flask对象
app = Flask(__name__)


# 进行关联
app.register_blueprint(blue_app1)
app.register_blueprint(blue_app2)




# 定义路由
@app.route("/")
def root():
    return "这是主页面"
    
    
app.run()

