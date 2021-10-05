# class Animal:   #父类
#     def eat(self,name):
#         self.name=name
#         print('【%s】开饭了'%self.name)
#     def drink(self,name):
#         self.name=name
#         print('【%s】在喝水'%self.name)
#
# class Cat(Animal):  #继承了Animal父类 此时Cat就是子类
#     def meow(self):
#         print('猫喵喵叫')
#
# class Dog(Animal):
#     def wow(self):
#         print('狗汪汪叫')
#
# d1=Dog()
# d1.eat('哈士奇')    #具备了eat的行为   继承了父类行为
# d1.wow()
# print('*'*30)
# c1=Cat()
# c1.drink('大橘')
# c1.meow()

#-------------------------多继承--------------------------
# class God:
#     def fly(self):
#         print('神会飞')
#
# class Monkey:
#     def eatPeach(self):
#         print('猴子爱吃桃')
#
# class Wukong(God,Monkey):   #孙悟空既是神仙 也是猴子
#     pass            #这里不写pass 编译器会认为下面的wk是本class内容 缩进不规范而报错
#
# wk=Wukong()
# wk.fly()
# wk.eatPeach()
#问题是 当多个父类中存在相同方法的时候 调用哪个呢
# class C:
#     def eat(self):
#         print('C.eat')
#
# class D(C):
#     def eat(self):
#         print('D.eat')
#
# class B(C):
#     pass
#
# class A(B,D):
#     pass
#
# a=A()
# a.eat()
# print(A.__mro__)    #可以显示类的依次继承关系 （执行顺序）
#在执行eat的方法时 查找方法的顺序是
#首先去A找 A中没有 则继续去B查找 B中没有 则去D中查找 D中没有 则去C查找 再找不到就报错
#A-B-D-C

#------------------------间接继承-------------------------
# class GrandFather:
#     def eat(self):
#         print('吃饭的某个方法')
#
# class Father(GrandFather):
#     def eat(self): #因为父类中已经存在这个的方法 在这里相当于 方法重写【方法覆盖了】
#         print('爸爸经常吃海鲜')
#     pass
#
# class Son(Father):
#     pass
#
# son=Son()
# print(Son.__mro__)
# son.eat()   #此方法是从GrandFather继承过来的
#总结：类的传递过程中 父类称为基类 字类称为派生类 父类的属性和方法可以逐级传递到子类

#----------------------------重写--------------------------------
class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print('汪汪叫')

class keji(Dog):
    def __init__(self,name,color): #重写了父类的方法
        #针对这种情况 就需要去调用父类的函数了
        # Dog.__init__(self,name,color)   #手动调用父类的方法 执行完毕就可以具备name和color这两个实例属性
        super().__init__(name,color)#另一种自动调用方法用super 自动找到父类 进而调用方法
                    #用super时要省略self，否则报错
                    #假设继承了多个父类 就会按照顺序逐个去找 然后再调用
        #拓展其它的属性
        self.height=90
        self.weight=20
        pass
    def __str__(self):
        return '{}的颜色是{} 身高是{}cm 体重是{}kg'.format(self.name,self.color,self.height,self.weight)
    def bark(self): #重写了父类的方法
        super().bark()  #调用父类的方法
        print('小声嘀咕')
        print(self.name)

kj=keji('柯基犬','红色')
kj.bark()
print(kj)
