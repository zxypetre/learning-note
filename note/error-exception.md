# 错误和异常
## 异常处理的介绍
* 异常处理，是编程语言或计算机硬件里的一种机制，用于处理软件或信息系统中出现的异常状况（即超出程序正常执行流程的某些特殊条件）。
* 通过异常处理，我们可以对用户在程序中的非法输入进行控制和提示，以防程序崩溃。
* 一段代码是异常安全的，如果这段代码运行时的失败不会产生有害后果，如内存泄露、存储数据混淆、或无效的输出。
## 常见的异常
1. NameError	尝试访问一个没有申明的变量
2. ZeroDivisionError	除数为0
3. SyntaxError	语法错误
4. IndexError	索引超出序列范围
5. KeyError	请求一个不存在的字典关键字
6. IOError	输入输出错误（比如你要读的文件不存在）
7. AttributeError	尝试访问未知的对象属性
```python
try:
    print(1)
except:
    print(2)
else:
    print(3)
finally
    print(4)
```
>如果正常，则打印1,3,4；如果异常打印2，4。
`except (ZeroDivisionError, ValueError) as e:`
`   print(e)`
>打印错误信息
### assert
assert是断言的意思,多用于以下情况：
1. 防御性的编程
2. 运行时对程序逻辑的检测
3. 合约性检查（比如前置条件，后置条件）
4. 程序中的常量
5.检查文档