#单例模式 是一种常用的软件设计模式 目的:确保某一个类只有一个实例存在
#如果希望在整个系统中 某个类只能出现一个实例的时候 那么这个单例对象就能满足要求

#创建一个单例对象 基于__new__去实现【推荐】
class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
       # cls._instance=cls.__new__(cls)   不能使用自身的new方法 容易造成深度递归
                                        #应该调用父类的new方法
       if not hasattr(cls,'_instance'): #如果不存在就开始创建
           cls._instance=super().__new__(cls,*args,**kwargs)
           return cls._instance
       else:
           return cls._instance
    pass
class DBoptSingle(DataBaseClass):
    pass

db1=DBoptSingle()
print(id(db1))
db2=DBoptSingle()
print(id(db2))
db3=DBoptSingle()
print(id(db3))

