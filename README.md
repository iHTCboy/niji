# NIJI

[![Build Status](https://travis-ci.org/ericls/niji.svg?branch=master)](https://travis-ci.org/ericls/niji) [![Documentation Status](https://readthedocs.org/projects/django-niji/badge/?version=latest)](http://django-niji.readthedocs.io/en/latest/?badge=latest)

Django-NIJI is a pluggable forum app for Django projects.

#### Demo
> https://demo.nijiforum.com/

#### Docs
> http://django-niji.rtfd.io


#### Run

1、cd到niji文件夹下（requirements.txt文件目录下），创建项目的虚拟环境：
```bash
virtualenv venv -p python3
```


2、激活venv环境：
```bash
source venv/bin/activate
```

3、安装 requirements.txt 运行环境依赖

```bash
pip3 install -r requirements.txt
```

4、创建数据库模型（ORM）

生成应用程序模型:
```python
python manage.py makemigrations
```

迁移模型到数据库：
```python
python manage.py migrate
```

5、 Admin 管理工具
可以通过网站链接后面增加admin，即 `http://yoursite/admin/` 访问管理后台

管理后台需要密码才能访问，通过下面命令创建超级用户：
```python
python manage.py createsuperuser
```

输入命令后，会提示输入`用户名`(区分大小写)，`邮箱`(方便django邮件通知管理员)，`密码`（不能设置太简单！），大概如下：
```bash
Username (leave blank to use 'niji'): HTC
Email address: ihetiancong@efun.com
Password:
Password (again):
Superuser created successfully.
```


6、django自带了一个简单的网络服务器。在开发过程中非常方便，通过执行命令来运行：
```bash
python manage.py runserver
```
- 注1：此命令需要在激活venv环境里执行，因为项目环境配置在venv环境下。
- 注2：此命令后面也可以带参数：IP地址和端口号 ```python manage.py runserver 172.0.0.1:1024```


7、运行成功后，浏览器打开 127.0.0.1:1024 就可以访问
```bash
System check identified no issues (0 silenced).
June 29, 2019 - 09:13:51
Django version 2.2.0, using settings 'settings'
Starting development server at http://172.0.1.1:1024/
Quit the server with CONTROL-C.
```