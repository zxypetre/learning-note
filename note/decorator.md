# 装饰器
利用装饰器获得函数执行时间代码：
```python
import time
from functools import wraps

def test1():
    print(2)
print('x')
def T(func):
    print(1)
    @wraps(func)
    def t(*args,**kwargs):
        #t0=time.strftime('%X')
        t1=time.time()suoyi
        f=func(*args,**kwargs)
        #t2=time.strftime('%X')
        t3=time.time()
        t=t3-t1
        print('{}执行花了{}s'.format(func.__name__,t))
        return f
    test1()
    return t

print(5)
@T
def test():
    for i in range(100):
        pass      

print(10)
test()
print(0)
```
@T相当于test = T(text),此时只执行了T函数，不过没有执行t函数，所以上面的打印顺序是：
output：x,5,1,2,10,text执行花了()s,0

* 装饰器相当于一个嵌套函数
* @wraps非常重要，如果没有@wraps，相当于改变了原函数__name__，它的作用等同与t.__name__ = func.__name__。
* *args可以代替多个参数.
* *kwargsk可以代替多个关键字参数