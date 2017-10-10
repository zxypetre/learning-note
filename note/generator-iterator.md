# 迭代器和生成器

1. 迭代器

     使用迭代器实现range功能代码如下：
```python
class _range(object):
    def __init__(self, start, stop=None):
        if stop == None:
            self.start,self.stop = -1,start
        else:
            self.start ,self.stop= start,stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start+1 >= self.stop:
            raise StopIteration
        self.start = self.start + 1
        return self.start
```
    实现斐波那契数列代码如下：
```python
class _range(object):
    def __init__(self, start=None):
        self.start = 0
        self.stop = 1
        self.a=start
        print(self.a)
    def __iter__(self):
        return self
    def __next__(self):
        if self.a==None:
            self.start = self.start + self.stop
            self.start,self.stop=self.stop,self.start
            return self.start
        if self.stop >= self.a:
            raise StopIteration
        self.start = self.start + self.sshultop
        self.start,self.stop=self.stop,self.start
        return self.start
```  

*   迭代器只能遍历一次对象。

2. 生成器

    使用生成器实现range功能代码如下：
```python
def _range(N):
    i = 0
    while i <N:
        yield i
        i=i+1
```
    使用生成器实现斐波那契数列代码如下：
```python
def _range(n):
    index = 0
    f0, f1 = 0, 1
    while index < n:
        yield f0
        f0, f1 = f1, f0 + f1
        index += 1
```

* 生成器的好处是延迟计算，一次返回一个结果。也就是说，它不会一次生成所有的结果，这对于大数据量处理，将会非常有用。
* 生成器还能有效提高代码可读性。
