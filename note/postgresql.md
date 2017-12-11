# POSTGRESQL
1. psql -u dbuser -d exampledb -h 127.0.0.1 -p 5432  进去控制台命令
    
    -u指定用户，-d指定数据库，-h指定服务器，-p指定端口
2. 控制台命令

    1. \h:查看sql命令的解释，比如\h select.
    2. \?:查看psql命令列表
    3. \l:列出所有数据库
    4. \c [database_name]:连接其他数据库
    5. \d:列出当前数据库的所有表格
    6. \d [table_name]:列出某张表格的结构
    7. \du:列出所有用户
    8. \e:打开文本编辑器
    9. \conninfo:列出当前数据库和连接消息   
3. 数据库操作

    1. create table tablename(key1 type1,key2 type2);   创建新表
    2. insert into tablename(key1,key2) values('value1','value2'); 插入数据
    3. select *(或者某个key) from tablename;  选择记录
    4. update tablename set key1 = 'newvalue' where key1 = 'oldvalue';   更新数据
    5. delete from tablename where name = 'value'; 删除记录
    6. alter table tablename add key3 type3; 添加表格的栏位
    7. alter table tablename alter column key set not null;   更新结构，可以用来设置限制 
    8. alter table tablename rename column key to key1;给表格栏位改名
    9. alter table tablename drop column key; 删除表格栏位
    10. alter table tablename rename to newname;给表格改名
    11. drop table if exists tablename;删除表格

4. 定义主键

    1. create table name(key1 primary key);  创建表格并将主键添加到表中
    2. 子句constraint name primary key(key);  指定主键
    3. alter table name add primary key(key);添加主键

5. 自动递增
    
    1. alter table name add column id serial； 设定id自动递增
