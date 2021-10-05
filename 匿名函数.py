#语法：
#lambda 参数1,参数2,参数三：表达式
#1. 使用lambda关键字去创建函数
#2. 没有名字
#3. 匿名函数冒号后面的表达式有且只有一个 是表达式 而不是语句
#4. 匿名函数自带return，而这个return的结果就是表达式计算后的结果
#缺点：lambda只能是单个表达式 不是一个代码块 lambda只适用于简单函数场景
#仅仅能封装有限的逻辑 无法实现复杂逻辑 否则必须用def处理
# def computer(x,y):
#     '''
#     计算数据和
#     :param x:
#     :param y:
#     :return:
#     '''
#     return x+y
#
# M=lambda x,y:x+y
# #通过变量去调用匿名函数
# print(M(23,19))

# result=lambda a,b,c:a*b*c
# print(result(12,34,2))

age=15
# print('可以参军'if age>18 else '继续上学')
#三目/三元运算符

funcTest=lambda x,y:x if x>y else y
print(funcTest(1,21))
#或者：
funcTest=(lambda x,y:x if x>y else y)(16,12)    #直接调用
print(funcTest)

var=lambda x:(x**2)+900
print(var(10))

