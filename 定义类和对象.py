#类结构：   类名  属性  方法
# class Person:
#     # name ='小张三' #类属性
#     age = 26      #类属性
#     def __init__(self):
#         self.name='张三'  #实例属性
#     def eat(self):  #类的内部定义一个实例方法 self为关键字（还可以是其他名字）
#         print('大口吃饭')
#     def run(self):  #类的内部定义一个实例方法
#         print('飞快的跑')

#创建一个对象（类的实例化）：
#规则格式：对象名=类名()
# zs=Person()
# zs.eat()    #调用函数
# zs.run()
# print('{}的年龄为{}。'.format(zs.name,zs.age))

# class People:
#     def eat(self):
#         print('喜欢吃榴莲')
# xq=People()
# xq.name='小茜'    #添加实例属性
# xq.age=20        #添加实例属性
# xq.eat()
# print(xq.name,xq.age)
#
# xl=People()
# xl.name='小李'
# xl.age=21

#init方法 初始化方法 实例化对象的时候在创建新对象时由系统自动调用（不需要手动调用） 完成一些初始化设置:
#系统自带的函数  注意要双下划线  【魔术方法】
# class People:
#     def eat(self):
#         print('喜欢吃榴莲')
#     def __init__(self):
#         self.name = '小茜'
#         self.age = 20
#
# xm=People()
# print(xm.name)   #直接输出的是默认值
# xm.name='小明'
# print(xm.name)   #已被修改成'小明'

#init传递参数 改进 使类更通用更方便更强大：
# class People:
#     def __init__(self,name,sex,age):    #传参
#         self.name=name
#         self.sex=sex
#         self.age=age
#     def eat(self,food):
#         self.food=food    #这条可省略
#         # print('{}喜欢吃{}'.format((self.name),(self.food)))
#         print(self.name,'like',self.food)
#         # print(self.name, 'like',food) 按上面省略的方法 输出就不能用self.food
#         print(self.name+'like to eat'+self.food)     #说明逗号和加号效果一样
#
# zp=People('zhang san','man','18')
# # print(zp.name,'-',zp.sex,'-',zp.age)
# zp.eat('Orange')

#-------------------------------关于self---------------------------------
#self和对象指向同一个内存地址 可以认为self就是对象的引用
#self只有在类中定义实例方法的时候才有意义 调用时不必传入相应的参数 而是由解释器自动去指向
#self的名字是可以更改的 可以定义成其他的名字 只是约定俗成地定义成了self
#self指的是类实例对象本身 相当于java中的this
# class Person:
#     def eat(self,name,food):
#         print('self=%s'%id(self))
#         # print('self=',id(self))   #另一种写法
#         print('%s like %s'%(name,food))
# xw=Person()
# print('xw=%s'%id(xw))
# xw.eat('laoban','juzi')

#-------------------------------魔术方法----------------------------------
#形如 __xxx__ 的内置方法
# class MethodTest:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#         print('---Test---init---')
#     def __str__(self):  #打印对象 自定义对象 是内容格式的
#         return '%s hat %se Haut.'%(self.name,self.color)
#     def __new__(cls, *args, **kwargs):  #创建对象实例的方法 每调用一次 就生成一个新对象
#         #cls class的缩写
#         #场景：可以控制创建对象的一些属性限定 经常用来做单例模式时候使用
#
#         print('---Test---new---')
#         return object.__new__(cls)  #在这里是真正创建对象实例的
#
# Hund=MethodTest('Luis','gelb')
# print(Hund)
#__new__ 和 __init__的区别：
#new：类的实例化方法 必须要返回该实例 否则对象创建不成功
#init:用来做数据属性的初始化工作 也可以认为是实例的构造方法 接受类的实例 self 并对其进行构造
#new：至少有一个参数是 cls 代表要实例化的类 此参数在实例化时由python解释器自动提供
#new函数执行会早于init函数

#作业（练习）：
#1. 通过类创建对象 用代码举例说明
#2. 在类中定义一个方法
# class Student:
#     def run(self):
#         print('学生每天跑步2000m')
#
# xl=Student()
# xl.run()

#3. 定义一个水果类 然后通过水果类 创建苹果对象 橘子对象 西瓜对象并分别添上颜色属性
# class Fruit:
#     def __init__(self,name,color):  #属性尽量在init中定义 不在class下定义
#         self.name=name
#         self.color=color    #左color（名字）和上color（参数）可以不一致
#     def __str__(self):
#         return '%s的颜色是【%s】'%(self.name,self.color)
#
# Apple=Fruit('苹果','红色')
# # Apple.radius=5    #添加一个半径属性到苹果对象中（通过对象去添加对象属性） 可行 但最好在类中去定义
# Orange=Fruit('橘子','黄色')
# Watermelon=Fruit('西瓜','绿色')
# print('*'*18)
# print(Apple)
# # print('苹果的半径为：',Apple.radius)
# print('*'*18)
# print(Orange)
# print('*'*18)
# print(Watermelon)
# print('*'*18)

#4. 编写代码 验证self就是实例本身
# class Person:
#     def weight(self):
#         print('self=%s'%id(self))
#
# lm=Person()
# lm.weight()
# print(id(lm))

#5. 定义一个Animal类
#(1) 使用__init__初始化方法为对象添加初始属性：颜色 名字 年龄
#(2) 定义动物方法：run eat 如xx在吃东西 即可
#(3) 定义一个__str__方法 输出对象的所有属性
# class Animal(object):
#     def __init__(self,color,name,age):
#         self.yanse = color    #证明了yanse这个名称不影响赋值 可以任意取名 传递的只是上面color参数
#         self.name = name
#         self.age = age
#     def run(self):
#         print('%s在狂奔'%self.name)    #单个参数 不需要加括号成：%(self.name)
#     def eat(self):
#         print('{}在吃东西'.format(self.name))   #换一种输出格式 不影响结果
#     def __str__(self):
#         return '【%s】的颜色是【%s】 年龄是【%s】岁'%(self.name,self.yanse,self.age)
#                                         #注意但是这里也要改成self.yanse 而不是self.color
# Dog=Animal('棕黄色','派克','12')
# print(Dog)
# Cat=Animal('粉红色','提莫','8')
# print(Cat)
# print('*'*35)
# Cat.run()
# Dog.eat()



