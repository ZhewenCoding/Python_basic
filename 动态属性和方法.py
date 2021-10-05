# import types    #添加方法的库
# def dynamicMethod(self):
#     print('{}的体重是：{}kg 学{}专业'.format(self.name,self.weight,Student.pro))
# @classmethod
# def classTest(cls):
#     print('这是一个类方法')
# @staticmethod
# def staticMethod():
#     print('这是一个静态方法')
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     pass
#     def __str__(self):
#         return '{}，今年{}岁'.format(self.name,self.age)
#     pass
#
# print('绑定类方法')
# Student.TestMethod=classTest
# Student.TestMethod()
#
# Student.staticMethodTest=staticMethod
# Student.staticMethodTest()
#
# zyh=Student('张友好',20)
# zyh.weight=80   #动态添加实例属性    但只是为zyh这个实例对象添加属性 不是为类对象
# zyh.printInfo=types.MethodType(dynamicMethod,zyh)   #动态的绑定方法
# zyh.TestMethod()
# # print(zyh)
# # print(zyh.weight)
# #-----------------另外一个实例对象 zm-------------------
# zm=Student('张敏',21)
# print(zm)
# # print(zm.weight)    #报错
# #-------------------给类对象添加属性---------------------
# Student.pro='自动化'   #动态添加类属性
# print(zm.pro,zyh.pro)
# #-------------------动态添加实例方法---------------------
# zyh.printInfo() #调用动态绑定的方法


#(P85 10-课后作业)
#练习：创建一个Animal类 实例化一个cat对象 给cat动态绑定一个run方法 给类绑定一个类属性color 给类绑定一个
#类方法打印字符串'ok'
import types
def run(self):  #在类外面定义一个run方法
    print('catrunrunrun')
@classmethod
def info(cls):
    print('Infos')
class Animal:
    pass
Animal.color='black'    #绑定类属性
Animal.dayinInfo=info
cat=Animal()
cat.run=types.MethodType(run,cat)   #给cat动态绑定一个run方法
cat.run()
print(cat.color)
Animal.dayinInfo()
