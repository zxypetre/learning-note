# redis
## redis的作用
Redis具有内置复制，Lua脚本，LRU驱逐，事务和不同级别的磁盘持久性，并通过Redis Sentinel提供高可用性，并通过Redis Cluster进行自动分区
## redis命令
1. redis-cli 进入redis数据库
2. set key value   创建一个键值对
3. get key   返回key对应的value
4. mset key1 value1 key2 value2  创建多个键值对
5. mget key1 key2 返回多个value
6. sadd key value  创建集合
7. smembers key 集合中key对应的value
## flask使用redis
    import redis   引入redis
    rdb = redis.(Strict)Redis(host='localhost',port=6379,db=0)
    rdb.set(key,value，ex=None, px=None, nx=False, xx=False)  
            在Redis中设置值，默认，不存在则创建，存在则修改
        参数：
            ex，过期时间（秒）
            px，过期时间（毫秒）
            nx，如果设置为True，则只有name不存在时，当前set操作才执行
            xx，如果设置为True，则只有name存在时，岗前set操作才执行

    rdb.mset(key1='value1',key2='value2'...)    
    rdb.get('key1')
    

