# class A():
#     def __init__(self):
#         print('__init__执行了')
#     def __new__(cls, *args, **kwargs):
#         print('__new执行了__')
#         return object.__new__(cls)
#
# a=A()

class Animal:
    def __init__(self):
        self.color='红色'
        pass
    #在python中 如果不重写 new默认结构如下
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args,**kwargs)
      #或return object.__new__(cls,*args,**kwargs)
    pass

tiger=Animal()  #实例化的过程会自动调用__new__去创建实例
#在新式类中 new才是真正实例化方法 为类提供外壳制造出实例框架
#然后调用该框架内的构造方法init进行丰满操作
#比喻建房子 new方法负责开发地皮 打地基 并将原料存放在工地
#而init负责从工地取材料建造出地皮开发图纸规定的大楼 负责细节设计 建造 最终完成
