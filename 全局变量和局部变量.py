def printInfo():
    name='peter'
def TestMethod():
    print(name)

# TestMethod()    #报错 name在TestMethod中没定义
# 函数内部定义的变量 作用域仅局限在函数内部
#不同的函数 可以定义相同的局部变量 互不影响
#局部变量作用:为了临时保存数据
#局部和全局相同时（重复定义时） 程序优先执行函数内部的变量（局部变量）【强龙不压地头蛇】
#在某个函数内部修改全局变量的方法（必须使用 global 关键字进行声明）：
#但对于列表/字典 允许在函数内部不加关键字直接修改
pro='自动化'
def changeGlobal():
    global pro
    pro='文学'

print(pro)
changeGlobal()  #如果不先运行一次该函数    全局变量不会被修改
print(pro)
