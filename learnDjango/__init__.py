"""常用命令
安装Django：	pip install django  指定版本 pip3 install django==2.0

新建项目：	django-admin.py startproject mysite

新建APP :	python manage.py startapp blog

启动：python manage.py runserver 8080

同步或者更改生成 数据库：

python manage.py makemigrations

python manage.py migrate

清空数据库：	python manage.py flush

创建管理员：	python manage.py createsuperuser

修改用户密码： python manage.py changepassword username

Django项目环境终端： python manage.py shell

这个命令和 直接运行 python 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据的测试非常方便。

更多关于Django的命令在终端输入：python manage.py 查看
"""

"""项目目录
learnDjango
    - learnDjango    # 对整个程序进行配置
    - init      #一个空文件，它告诉Python这个目录应该被看做一个Python包
    - settings    # 项目配置文件
    - url      # URL对应关系（路由）
    - wsgi     # 遵循WSIG规范，uwsgi + nginx
- manage.py     # 一个命令行工具，可以使你用多种方式对Django项目进行交互
"""

"""APP目录
blog                 #应用目录
│  admin.py        #对应应用后台管理配置文件。
│  apps.py         #对应应用的配置文件。
│  models.py       #数据模块，数据库设计就在此文件中设计。后面重点讲解
│  tests.py        #自动化测试模块，可在里面编写测试脚本自动化测试
│  views.py        #视图文件，用来执行响应代码的。你在浏览器所见所得都是它处理的。
│  __init__.py
│
├─migrations        #数据迁移、移植文目录，记录数据库操作记录，内容自动生成。
│  │  __init__.py
"""