# AmyYoga
这是一个大学课设项目，github仅用于版本控制
## 简介
此系统为Amy瑜伽馆信息管理系统，系统功能由瑜伽教练Amy与HITWH开发团队 起这个名字花了我5分钟（Cost me Five Minutes） 共同设计。
## 系统特色功能
* 会员信息管理
* 身体评估报告管理与时间线显示方式
* 消费记录查询
## 系统部署
目前使用Apache2 服务器部署于http://srcserver.xyz

## 系统部署方法
使用venv虚拟运行环境，语言Python3.7.1版本及以上，AmyYoga代码文件夹放置在/var/www/路径下，apache2服务器配置文件内容：
```
<VirtualHost *:<port>>
    ServerName localhost:<port>
    ServerAdmin <管理员邮箱>  

    WSGIScriptAlias / /var/www/AmyYoga/AmyYoga/wsgi.py
    WSGIDaemonProcess <主机名> python-home=<venv路径>/var/venv python-path=/var/www/AmyYoga
    WSGIProcessGroup <主机名>
    Alias /static/ /var/www/AmyYoga/collected_static/
    <Directory /var/www/AmyYoga/collected_static>
        Require all granted
    </Directory>
    <Directory /var/www/AmyYoga/AmyYoga>
	    <Files wsgi.py>
	        Require all granted
	    </Files>
    </Directory>
</VirtualHost>
```
