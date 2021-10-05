# import 模块制作             #第一种方法
#
# res1=模块制作.add(2,4)
# res2=模块制作.diff(5,1)
# print(res1,res2)
# print(模块制作.printInfo())   #__all__不影响其调用

# from 模块制作 import add    #第二种方法

from 模块制作 import *      #第三种方法
print(add(15,2))
print(diff(22,1))
# printInfo()             #报错 name 'printInfo' is not defined
                        # 因为__all__函数的关系 不能被调用(仅限*情形)


