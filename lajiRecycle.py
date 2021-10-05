import sys
import psutil
import os
def showMemSize(tag):
    pid=os.getpid()
    p=psutil.Process(pid)
    info=p.memory_full_info()
    memory=info.uss/1024/1024
    print('{}memory used:{} MB'.format(tag,memory))
    pass

#验证循环引用的情况
def func():
    showMemSize('初始化')
    a=[i for i in range(1000000)]
    b=[i for i in range(1000000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象 a b 之后')
    pass
func()
showMemSize('完成时候的')
# sys.getrefcount()
# a=[]
# print(sys.getrefcount(a))   #输出a被引用的次数 结果为2
# b=a
# print(sys.getrefcount(a))   #3次
# c=b
# d=b
# e=c
# f=e
# g=d
# print(sys.getrefcount(a))   #8次

