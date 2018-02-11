1. man 查看命令的帮助文档
2. free 查看电脑内存
3. rm 删除
4. mv  移动和重命名
5. ll  查看文件夹里的文件位文件夹还是文件  以d开头的是文件夹     以-开头的是文件
6. help   获取帮助信息
7. pip   安装
8. ctrl-w  删除键入的最后一个单词；ctrl-u(k) 删除行内光标所在z位置之前(后)的内容；ctrl-a(e) 将光标移到行首(末)；ctrl-l  清屏；alt-b(f) 以单词为单位移动光标；
9. history 查看命令行历史记录
；!n(n是命令编号)就可以再次执行了；!$指代上次键入的参数；!!指代上次键入的命令；这些功能可以通过ctrl-r和alt-.来实现。
10. cd - 回到上一个工作路径
11. cd ~ 回到home目录
12. kill -stop[] 停止一个进程
13. nohup或者disown 使一个后台进程持续运行
14. uptime 查看系统运行多次时间
15. alias 创建常用命令的快捷形式
16. tail 默认输出文件后10行内容；tail -n file   输出文件后n行，tail -n+k file 从文件第k行开始输出;tail -f file 动态跟踪文件file的增长情况，tail会每隔一秒检查一下文件是否增加了新内容
17. apt-get 用于自动从互联网的软件仓库中搜索、安装、升级、卸载软件或操作系统。
    1. -f 尝试修正系统依赖损坏处
18. 1. echo hello>>text.txt   将hello添加到text.txt文本末尾
    2. echo hello>text.txt 将text.txt的内容替换成hello
19. chmod命令用于改变linux系统文件或目录的访问权限。用它控制文件或目录的访问权限。该命令有两种用法。一种是包含字母和操作符表达式的文字设定法；另一种是包含数字的数字设定法。
    1. 权限代号： 
        1. r:读权限，数字4表示
        2. w:写权限，数字2表示
        3. x:执行权限，数字1表示
        4. -:删除权限，数字0表示
        5. s:特殊权限
    2. 权限范围
        1. u：目录或者文件的当前的用户
        2. g：目录或者文件的当前的群组
        3. o：除了目录或者文件的当前用户或群组之外的用户或者群组
        4. a：所有的用户及群组
    3. 文字设定法
        chmod ［who］ ［+ | - | =］ ［mode］ 文件名
    4. 数字设定法
        1. chmod ［mode］ 文件名
        2. 数字与字符对应关系：
+                 r=4，w=2，x=1
+                 若要rwx属性则4+2+1=7
+                 若要rw-属性则4+2=6；
+                 若要r-x属性 则4+1=7。 
20. 1. dpkg -i package.deb	安装包
    2. dpkg -r package	删除包
    3. dpkg -P package	删除包（包括配置文件）
    4. dpkg -L package	列出与该包关联的文件
    5. dpkg -l package	显示该包的版本
    6. dpkg –unpack package.deb	解开 deb 包的内容
    7. dpkg -S keyword	搜索所属的包内容
    8. dpkg -l	列出当前已安装的包
    9. dpkg -c package.deb	列出 deb 包的内容
    10. dpkg –configure package	配置包
    
    11. dpkg --force-confmiss -i /var/cache/apt/archives/nginx-common_*.deb   将丢失的包补回来
