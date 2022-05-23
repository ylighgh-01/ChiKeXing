# 吃客行网站重构

Web期末作业

## 使用

安装依赖:`pip install -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple/`

运行：
1. `export FLASK_APP=app.py`
2. `flask run --host=0.0.0.0`

后台运行: `nohup flask run --host=0.0.0.0 > myweb.log 2>&1 &`

访问:`http://localhost:5000`

## 需求分析

1. **登录/注册**
2. **发布菜品**
3. **展示菜品**
4. **查找菜品**
5. **删除菜品**
6. **用户个人中心**

## 技术选型

前端: 

- 三件套 HTML+CSS+JavaScript
- 组件库 BootStrap

后端:
- Python 3.10
- Flask(web框架)
- MySQL 5.7 

部署: 
-  Nginx+FastCGI
