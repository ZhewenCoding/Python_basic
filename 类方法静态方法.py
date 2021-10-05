#------------------------类方法---------------------------
# class People:
#     country='China'
#     @classmethod    #类方法 用classmethod来修饰
#     def get_country(cls):
#         return cls.country  #访问类属性
#         pass
#     @classmethod
#     def change_country(cls,data):
#         cls.country=data    #在类方法中修改类属性的值
#     pass
#     @staticmethod
#     def getData():  #不带参数的静态方法
#         return People.country     #通过类对象去引用
#     @staticmethod
#     def add(x,y):   #带参数的静态方法
#         return x+y
#         pass
#
# print(People.add(1,2))
# print(People.getData())
# p=People()
# print(p.getData())  #一般情况下 不会通过实例对象去访问静态方法 因为去实例化对象要耗费资源
#为什么要使用静态方法：
#由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互
#也就是说 在静态方法中 不会涉及到类中方法和属性的操作
#数据资源能得到有效 充分的利用
#静态方法举例：
# import time     #引入第三方时间模块
# class TimeTest:
#     def __init__(self,hour,min,second):
#         self.hour=hour
#         self.min=min
#         self.second=second
#     @staticmethod
#     def showTime():     #静态方法功能通常是独立的
#         return time.strftime('%H:%M:%S',time.localtime())
#         pass
#     pass
#
# print(TimeTest.showTime())
# #或者：
# t=TimeTest(2,1,3)
# print(t.showTime())     #没有必要用这种方式访问静态方法


# print(People.get_country()) #通过类对象去引用
# p=People()
# print('实例对象访问 %s'%p.get_country())
# print('修改后：')
# People.change_country('Korea')
# print(People.get_country())
# print('实例对象访问 %s'%p.get_country())

#三种方法的比较：
#1.类方法  类方法的第一个参数是类对象 cls 进而去引用类对象的属性和方法
#必须用装饰器@classmethod修饰
#2.实例方法的第一个参数必须是self 通过这个self可以去引用类属性或者实例属性 若存在
#相同名称实例属性和类属性的话 实例属性的优先级最高
#3.静态方法不需要定义额外的参数 若是要引用属性的话 则可以通过类对象或者实例对象去引用
#必须用@staticmethod修饰

#--------------------------私有化方法-----------------------------

class Animal:
    def __eat(self):
        print('吃东西')
        pass
    def run(self):
        self.__eat()    #在此调用私有化方法
        print('飞快地跑')
    pass
class Bird(Animal):
    pass

b1=Bird()
# b1.__eat()  #报错 'Bird' object has no attribute '__eat'
b1.run()
