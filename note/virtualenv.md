# virtualenv
## virtualenv用于创建独立的Python环境，多个Python相互独立，互不影响，它能够：
    1. 在没有权限的情况下安装新套件
    2. 不同应用可以使用不同的套件版本
    3. 套件升级不影响其他应用
## 安装
+ sudo apt-get install python-virtualenv
## virtualenv的使用
1. virtualenv [虚拟环境名称]  (创建虚拟环境)
2. source venv/bin/activate    (启动虚拟环境)
3. deactivate   (退出虚拟环境)
4. pip install [套件名称]  (安装pip套件)
5. --no-site-packages：不使用系统环境的python安装包，即隔离包中不能使用真实python环境的安装包；当前版本这个选项是默认的。
6. --system-site-packages：与上面相反，使隔离环境能访问系统环境的python安装包
7. --distribute：copy一个python环境的分支，默认会安装setup、pip、wheel等基础模块