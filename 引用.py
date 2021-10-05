a=1     #不可变类型
def func(x):
    print('x的地址：{}'.format(id(x)))
    x=2
    print('x的值修改后地址：{}'.format(id(x)))
    print(x)

print('a的地址：{}'.format(id(a)))
func(a)
print(a)

#可变类型
li=[]
def testRenc(parms):
    li.append([1,3,5245,11])
    print(id(parms))
    print('内部的{}'.format(parms))

print(id(li))
testRenc(li)
print('外部的变量对象{}'.format(li))

#1. 在Python中 万物皆对象 在函数调用的时候 实参传递的就是对象的引用
#2. 了解了原理之后 就可以更好的去把控 在函数内部的处理是否会影响到函数外部的数据变化
#参数的传递是通过对象引用来完成的