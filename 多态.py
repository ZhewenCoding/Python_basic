class Animal:
    def say_who(self):
        print('我是小动物')
        pass
    pass

class Duck(Animal):
    def say_who(self):  #在这里重写父类的方法
        print('是一只鸭子')
    pass
class Dog(Animal):
    def say_who(self):
        print('是一只狗狗')
    pass
class Cat(Animal):
    def say_who(self):
        print('是一只猫咪')
    pass
class Bird(Animal):     #新增鸟类
    def say_who(self):
        print('是一只小鸟')
    pass
class Student(Animal):  #新增人类
    def say_who(self):
        print('是一个学生')
    pass
def commonInvoke(obj):     #统一调用的方法 （体现多态）只要class里有这个方法 就能被统一调用
    obj.say_who()          #只要关注这个函数方法  不需要关注对象类型

# duck1=Duck()
# duck1.say_who()
# dog1=Dog()
# dog1.say_who()
# cat1=Cat()
# cat1.say_who()

listObj=[Duck(),Dog(),Cat(),Bird(),Student()]     #新增鸟类
for item in listObj:
    commonInvoke(item)

#多态的好处：
#增加程序的灵活性 拓展性
#鸭子类型（duck typing）
#在鸭子类型中 关注的不是对象的类型本身 而是它是如何使用的
#本例中 指的是 只要方法看起来都是say_who() 就可以被统一调用
