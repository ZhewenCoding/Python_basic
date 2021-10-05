#作用：限制要添加的实例属性 节约内存资源
class Student():
    __slots__ = ('name','age')
    def __str__(self):
        return '{}....{}'.format(self.name,self.age)

# xw=Student()
# xw.name='小王'
# xw.age=20
# xw.weight=60        #由于被slots函数限制 weight属性不能被添加
# print(xw)
# print(xw.__dict__)    #所有可以用的属性都在这里存储 注释掉slots才能调用
                      #不足的地方就是dict占用的空间内存大
# print(xw.weight)    # 报错
#总结：定义slots变量后 Student类的实例已经不能随意创建不在slots中定义过的属性了
#同时实例中也不能再有__dict__

#在继承关系中slots的使用:
#当子类未声明slots时 是不会继承父类的slots的 此时子类是可以随意属性赋值的 如gender pro
#当子类声明slots时 继承父类的slots 即子类slots的范围是自身+父类的slots范围（并集）
class subStudent(Student):
    __slots__ = ('gender','pro')    #不要再去重复写父类中的限定项 name age 占用空间
    pass
ln=subStudent()
ln.gender='男'
ln.pro='计算机'
ln.name='李宁'    #name和age这两个可定义范围 从父类Student继承而来
ln.age=23
print(ln.gender,ln.pro,ln.age,ln.name)



