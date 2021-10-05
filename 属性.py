#类属性和实例属性
# class Student:
#     name='小李'   #类属性 由Student类对象所拥有
#     def __init__(self,age):
#         self.age=age    #实例属性
#
# xl=Student(23)
# print(xl.name)  #通过实例对象去访问类属性
# print(xl.age)   #通过实例对象去访问实例属性
# aw=Student(24)
# print(aw.name)
# print(aw.age)
#                 #通过实例对象对类属性进行修改 可以吗？↓
# aw.name='阿伟'   #是通过实例对象去引用的 修改的是实例属性 不会影响类属性 （无权修改类属性）
# Student.name='阿超'   #这里通过类对象去引用的name 修改后类属性name被改成了阿超
# print(aw.name)
# print(Student.name)
# print(xl.name)  #这行 证明了类属性name被修改成了阿超
# print(Student.name) #通过类对象去访问类属性    类名.属性名 形式去访问
# print(Student.age)  #通过类对象去访问实例属性   报错  （不能访问）
#小结：类属性可以被类对象和实例对象共用访问使用    实例属性只能由实例对象访问使用

#---------------------------属性私有化----------------------------
#使用场景：
#隐藏一个特定属性 不想让类的外部直接调用
#保护一个属性 不让属性的值随意改变
#保护一个属性 不让派生类【子类】去继承

# class Person:
#     __hobby='跳舞'    #变成私有的类属性
#
#     def __init__(self):
#         self.__name='李四'    #加两个下划线 将此属性私有化 之后便不能从外部直接访问 当然在类内部可以访问
#         self.age=30
#         pass
#     def __str__(self):       #私有化的属性在内部可以使用self.__name
#         return '{}的年龄是{} 爱好是{}'.format(self.__name,self.age,Person.__hobby)
#     def changeValue(self):
#         Person.__hobby='唱歌'
# class Student(Person):
#     def printInfo(self):
#         # print(self.__name)   #在此访问父类中的私有属性 可以吗？   不可以
#         print(self.age)
#     pass

# stu=Student()
# print(stu.__name)
# stu.printInfo()
# stu.changeValue()   #修改私有属性
# print(stu)
# print(stu.__hobby)    #实例对象访问类属性
# print(Person.__hobby) #类对象访问类属性
# xl=Person()
# print(xl)
# print(Person.age)
# print(Person.__name)
# print(Person.__name)#类对象不能访问私有属性
# print(xl.__name)  #实例对象不能访问私有属性

#小结：
#私有化的实例属性和类属性 都不能在外部直接访问 但可以在类的内部随意使用
#子类不能继承父类的私有化属性 只能继承父类公共的属性和行为
#在属性名前面加两个下划线 __ 就可以私有化了

#--------------------------属性函数----------------------------
#实现方式一：调用property函数
# class Person(object):
#     def __init__(self):
#         self.__age = 18     #自己的理解：因为是私有化属性 所以上一行不需要给形参
#     def get_age(self):
#         return self.__age
#     def set_age(self,age):  #对比上面注释 这里是非私有化参数 所以要给出形参
#         if age < 0:
#             print('年龄不能小于0')
#         else:
#             self.__age = age
#         pass
#     # 定义一个类属性 实现通过直接访问属性的形式去访问私有属性
#     age=property(get_age,set_age)
#     pass
#
# #实现方式二：通过装饰器的方式去声明
#     @property   #用装饰器修饰 添加属性标识 提供一个getter方法
#     def age(self):
#         return self.__age
#     @age.setter #用装饰器修饰 提供一个setter方法
#     def age(self,parms):
#         if parms < 0:
#             print('年龄不能小于0')
#         else:
#             self.__age=parms
#             pass
#         pass
#
#
# p1=Person()
# print(p1.age)
# p1.age=30
# print(p1.age)
# # print(p1.set_age)

#--------------------属性私有化练习------------------------
#1. 编写一段代码满足以下要求：
#定义一个Person类 类中要有初始化方法 方法中要有人的姓名 年龄两个私有属性
#提供获取用户信息的函数
#提供获取私有属性的方法
#提供可以设置私有属性的方法
#设置年龄的范围在(0-120)的方法 如果不在这个范围内 不能设置成功

# class Person:
#     def __init__(self,__name,__age):
#         self.__name=__name
#         self.__age=__age
#     def __str__(self):
#         return '{}的年龄是{}'.format(self.__name,self.__age)
#     def getNameInfo(self):
#         return self.__name
#     def setName(self,name):
#         self.__name=name
#     def getAgeInfo(self):
#         return self.__age
#     def setAge(self,age):
#         if age >= 0 and age <= 120:
#             self.__age=age
#         else:
#             print('年龄不合理')
#
# zs=Person('张三',18)
# print(zs)
# zs.setName('小王')
# print(zs)
# zs.setAge(15)
# print(zs)
# zs.setAge(153)


#2. 创建一个类 定义两个私有化属性 提供一个获取属性的方法 一个设置属性的方法 利用property属性给调用者提供
#属性方式的调用
#用装饰器时：
# class Student:
#     def __init__(self):
#         self.__name='Cokki'
#         self.__score=85
#     @property
#     def name(self):   #用装饰器时 函数名要和变量名一致 本例为name和score
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self,score):
#         self.__score=score
#     # def __str__(self):
#     #     return self.__name
#     def __call__(self, *args, **kwargs):
#         print('{}的得分是{}'.format(self.__name,self.__score))
#
# xw=Student()
# xw()
# xw.name='Passa'
# xw.score=96
# xw()
# print(xw)

#用property函数时：
class Student:
    def __init__(self):
        self.__name='Cokki'
        self.__score=85
    def get_name(self):     #用property函数时 不需要函数名和变量名相同
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score=score
    def __str__(self):      #输出return只能为字符串 凡是return 必须用print才能显示 直接调用不显示
        # return '{}的得分是:{}'.format(self.__name,self.__score)   #可行
        return self.__name+'的得分是:'+str(self.__score)            #可行
        # return self.__name,'的得分是:',self.__score     #不能用逗号连接 被当作了Tupel而报错
    # def __call__(self, *args, **kwargs):
    #     print('{}的得分是{}'.format(self.__name,self.__score))

    name=property(get_name,set_name)    #将私有变公有
    score=property(get_score,set_score) #本行和上行注释掉后 则下面的修改无效 但不会报错

xw=Student()
# xw()
xw.name='Kacci'
xw.score=76
# xw()
print(xw)