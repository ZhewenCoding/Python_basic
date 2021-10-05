#优化代码方案：封装函数
# print('测试封装函数用')
# print('----line2----')

# def printInfo(name,ID):
#     '''本函数是用来测试调用的''' #备注信息 悬停有效
#     print('测试封装函数用:')
#     print('%s直播间的ID是：%s'%(name,ID))
#     print('----line2----')
#
# #调用函数：
# printInfo('up主','21593493')
#
# #加入传入参数：name,ID（如上）
#
# #函数参数：
#     #1.必选参数 调用时必须给值 否则报错
# def sum(a,b): #形式参数 定义时不占用内存地址
#     sum=a+b
#     print(sum)
#
# sum(3,9) #实际参数 占用内存地址
# # sum()   #报错 丢失a,b两个数据
#     #2.默认参数 （缺省参数）
# def sum1(c=15,d=4):
#     print('默认参数=%d'%(c+d))
#
# sum1()
# sum1(10) #在调用的时候如果为赋值 会用定义函数时给定的默认值
#
#     #3.可选参数 当参数的个数不确定时使用 较灵活   接受的数据为元组类型
# def getComputer(*args): #*args固定写法 表示可变长的参数
#     print(args)
#
# getComputer(1)
# getComputer(1,2)
# getComputer('hi')
#输出都为元组类型

# def getSum(*args):   #args: arguments 参数
#     result=0
#     for item in args:
#         result+=item
#     print('result=%d'%result)
#
# getSum(1)
# getSum(1,2)
# getSum(1,2,3)
#
# getSum(1.23,1.999) #是int型 小数位被抹去了 结果为2

#问题：怎么转换成folat型？  恍然大悟，print里输出模式改成%f即可

#测试输出str类型（做求和）：
# def getSum(*args):
#     result=0
#     for item in args:
#         result+=item
#     print('result=%s'%result)
#
# getSum('h','i')   #报错 说明自增不适用于str类型！
        #4.关键字可变参数  用**来定义
#在函数体内 参数关键字是一个dict字典类型 key是一个字符串
# def keyFunc(**kwargs):  #kwargs: keywords arguments 接受的数据为字典类型
#     print(kwargs)

# keyFunc(1,2,3)  #报错  不能传递
# dictA={'name':'Jay Chou','age':18}
# print('当前字典为:',(dictA))

# keyFunc(**dictA)    #直接调用函数时 必须加** 否则报错
# keyFunc(name='Jason Mraz',age=35) #以命名参数的形式传递

# def complexFunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# complexFunc()
# complexFunc(1,2,3,4,5)
# complexFunc(2,3,3,name='Eason Chan',age=39)
# complexFunc(name='Eason Chan',age=39)
# complexFunc(ID=114)
# print(dictA)

# def Test01(**kwargs,*args):   #报错  因为args必须放到kwargs之前
    #...

#-----------------------函数返回值-------------------------
# def Sum(a,b):
#     sum=a+b
#     return sum
#
# print(Sum(10,20))
# #或：
# rs=Sum(10,20)
# print(rs)

# def calComputer(num):
#     result=0
#     i=1
#     while i<=num:
#         result+=i
#         i+=1
#     return result
#
# print(calComputer(10))
# #或：
# value=calComputer(10)
# print(type(value))
# print(value)

#改成 以list列表形式返回：
# def calComputer(num):
#     result=0
#     i=1
#     list1=[]
#     while i<=num:
#         result+=i
#         i+=1
#     list1.append(result)
#     return list1
#
# print(calComputer(10))
# print(type(calComputer(10)))   #返回一个list类型
#
# 返回一个元组/字典
# def returnTuple():
#     return 1,23,34
#
# print(type(returnTuple()))
#
# def returnDict():
#     return {'name':'Wugui'}
#
# print(type(returnDict()))

# #-------------------------函数嵌套----------------------------
# def fun1():
#     print('----------一个有趣的 无内容的函数-----------')
#
# def fun2():
#     print('----------一个无趣的 有内容的函数-----------')
#     fun1()                  #嵌套
#     print('----------一个无趣的 有内容的函数-----------')
#
# #调用fun2:
# fun2()

#练习：
#1. 写函数，接收n个数字，求这些参数数字的和
# def Sum1():
#     n=1
#     sum=0
#     while n <= 5:
#         Nums=int(input('请依次输入所有数字，并以回车确认：'))
#         sum+=Nums
#         n+=1
#     print('经计算，所有数字之和为：',sum)
#
# Sum1()

#参考程序：
# def Sum1(*args):
#     result=0
#     for item in args:
#         result+=item
#     return result
#
# rs=Sum1(1.5,2,3,4,5,6,7,8,9)  #用rs变量来接收返回值
# print('rs={}'.format(rs))
# print('rs=%f'%rs)
#两种print都可以

#1.5.改成for循环
# def Sum1():
#     n=1
#     for        #改不了 因为for适用于已经有可迭代的集合对象的情形
#                #除非先储存全部输入的数字，再命名为一个集合，再用for循环
#
# Sum1()

#2. 求上题中的奇数和
# def OddSum1():
#     n=1
#     sum=0
#     while n<=5:
#         Nums = int(input('请依次输入所有数字，并以回车确认：'))
#         if Nums % 2 == 1:     #如果为奇数
#             sum+=Nums
#         n+=1
#     print('经计算，所有奇数之和为：',sum)
#
# OddSum1()

#3. 写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
#假定已有一组数据（list/tuple）:
# list1=[1,2,3,4,5,6,7]
# def RenewOddList1():
#     list2=list1[1::2]   #一开始想到的是用循环挨个取出奇数位上元素再合并
#     return list2        #但是切片操作更合适 因为切片就是为了实现这个功能的
#
# print(RenewOddList1())

#让用户手动输入list的每个元素，自动整合成一个list:
# def RenewOddList1():
#     print('请输入list中的每个元素，并以回车键结束，全部输入完毕输入[Yes]确认：')
#     i=0
#     list1=[]
#     #while i < 10:    #用户最多输入10个元素
#     while i>-1:     #用户可以无限制地输入i个元素，直到以Yes确认
#         item=input()
#         if item == 'Yes' or item == 'yes' or item == 'Y' or item == 'y':
#             break
#         list1.insert(i,item)
#         i += 1
#     print('您输入的list为：')
#     print(list1)
#     listNew=list1[1::2]
#     print('删除偶数项后的list为：')
#     return listNew
#
# print(RenewOddList1())

#参考程序：
# def RenewOddList1(contain):
#     '''
#     处理接收的数据
#     :param contain: 可变长的参数 可以接受一个元组
#     :return:    计算和
#     '''
#     listNew=[]
#     index=1
#     for i in contain:
#         if index % 2 == 1:
#             listNew.append(i)
#         index+=1
#     return listNew

# rs2=RenewOddList1([1,2,3,4,5,6,7,8,9,10])
# print(rs2)
#或者下面方法：
# rs2=RenewOddList1(tuple(range(10,30)))  #把元组的数据添加到list中
# print(rs2)

#4. 写函数，检查传入字典的每一个value的长度，如果大于2，
#4. 则仅保留前两个长度的内容，并将新的内容返回给调用者
# def CheckLength(**kwargs):   #或直接写一个变量
#     '''
#     处理字典类型的数据
#     :param kwargs:  字典
#     :return:
#     '''
#     dict1={}
#     i=0
#     print('请输入字典元素')
#     while i > -1:
#         item=input()

# def CheckLength(dicParms):  #**kwargs
#     '''
#     处理字典类型的数据
#     :param kwargs:  字典
#     :return:
#     '''
#     result={}   #空字典
#     for key,value in dicParms.items(): #for循环去遍历 直接获取字典的项 包含key和value
#         if len(value) > 2:
#             result[key]=value[:2]   #切片 输出第0位到第2位前（即第1位）的
#         else:
#             result[key]=value
#     return result
# #为什么268/270行把右边的value赋值给左边的key？
# dict1={'name':'某某','hobby':['唱','跳','rap','篮球'],'pro':'艺术专业'}
# CheckLength(dict1)
# print(CheckLength(dict1))

# def myprint():
#     print("-" * 20)
#
# myprint()


#------------------------------内置函数----------------------------------
# print(abs(-2))  #取绝对值
# print(round(3.666))
# print(round(3.666,2))   #取近似值（四舍五入）
# print(pow(3,3)) #求次方
# print(3**3)
# print(divmod(7,3))  #求商和余数 返回一个元组
# print(max([23,151,124115,1223,112]))
# print(max(23,151,124115,1223,112))  #取最大值
# print(sum(range(50)))
# print(sum(range(50),3)) #求和
# a,b,c=1,2,3
# print('动态执行的函数={}'.format(eval('a+b+c')))   #eval 动态执行函数
# print('动态执行的函数={}'.format(eval('a*b+2*c+1')))   #eval 动态执行函数
#
# def TestFun():
#     print('我执行了吗？')
#
# eval('TestFun()')   #可以调用函数执行
#
# print(eval('a+b+c',{'c':3,'a':1,'b':3}))    #global变量作用域 如果被提供 必须是字典对象
#
# #类型转换函数：
# print(bin(10))  #转换二进制
# print(hex(23))  #转换十六进制
# tup=(1,2,3,4)
# li=list(tup)    #元组转换成list
# print(li)
# li.append('success')
# print(li)
# tupList=tuple(li)   #list转换成tuple
# print(type(tupList))
# print(tupList)
# dic=dict(age=18)      #创建一个字典
# print(type(dic))
# dic['name']='xDD'
# print(dic)
# print(bytes('我喜欢吃面',encoding='utf-8'))  #转换为字节码
#
# print(all(()))      #result:bool
# print(all([]))
# print(all({}))
# print(all([1,2,3,0]))
# print(all([1,2,3,False]))
#
# print(any((0,1,2)))
# print(any(('',False,0)))    #any() 类似于逻辑运算符or 只要有一个True 结果就为True
#
# li=[2,45,15,133,1] #原始对象
# # li.sort()          #list的排序方法 直接修改原始对象
# print('排序之前：{}'.format(li))
# li2=sorted(li)                  #升序排列（默认）
# print('排序之后：{}'.format(li2))
# li2=sorted(li,reverse=True)     #降序排列
# print('排序之后：{}'.format(li2))
# s1=['a','b','c']
# s2=['你','我','他']
# s3=['你','我','他','X','Y']
# print(zip(s1))      #zip() 用来打包 会把序列中对应的索引位置的元素储存为一个元组 本条显示zip存储位置（无实用）
# print(list(zip(s1)))    #将压缩的元组转换成list 并输出
# zipList=zip(s1,s2)      #压缩两个参数
# print(list(zipList))    #将压缩的元组转换成list 并输出
# zipList=zip(s1,s3)    #压缩两个参数
# print(list(zipList))  #将压缩的元组转换成list 并输出
#实例：
# def printBookInfo():
#     books=[]    #存储所有的图书信息
#     id=input('请输入编号：每个项以空格分隔')
#     bookName=input('请输入书名：每个项以空格分隔')
#     bookPos=input('请输入位置：每个项以空格分隔')
#     idList=id.split(' ')        #分隔
#     nameList=bookName.split(' ')
#     posList=bookPos.split(' ')
#
#     bookInfo=zip(idList,nameList,posList)   #打包处理
#     for bookItem in bookInfo:
#         '''
#         遍历图书信息进行存储
#         '''
#         dictInfo={'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
#         books.append(dictInfo)  #将字典对象添加到list容器中
#     for item in books:
#         print(item)
# #362-363不太懂
# printBookInfo()

#测试split():
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# print(str)
# print(str.split( ))
# print(str.split(' ', 1 ))

# listObj=['a','b','c']
# for item in enumerate(listObj): #enumerate()作用是加索引0,1,2,...
#     print(item)                 #输出是元组类型
#
# #改输出类型：
# for index,item in enumerate(listObj):
#     print(index,'--',item)
#
# #改初始索引号：
# for index,item in enumerate(listObj,5):
#     print(index,'--',item)

#用enumerate()遍历字典：
# dictObj={}
# dictObj['name']='Jay'
# dictObj['hobby']='singing'
# dictObj['pro']='artist'
# print(dictObj)
# for index,item in enumerate(dictObj):
#     print(item)
# print(dictObj.items())

#函数练习：
#1. 求三组连续自然数的和 求出1-10 20-30 35-45的和
#要构建一个通用函数！
#思考 用sum函数 用range生成序列  不需要外部输入  需要计算后内部输出
# print(sum(range(11)))
# print(sum(range(20,31)))
# print(sum(range(35,46)))

# def Sum1():
#     a=int(input('请输入首位数'))
#     b=int(input('请输入末位数'))
#     if a < b:
#         print('连续求和结果为：',sum(range(a,b+1)))
#     else:
#         print('参数不正确')

# Sum1()
#2. 100个和尚吃100个馒头 大和尚一人吃3个馒头 小和尚三人吃一个馒头 请问大小和尚各多少人？
# def CountManTou():   #大和尚人数：a    小和尚人数：100-a
#     for a in range(1,101):
#         if a*3+(100-a)*(1/3) == 100:
#             return (a,100-a)
#
# Result=CountManTou()
# # print('大和尚{} 小和尚{}'.format(Result,(100-Result)))
# print('大和尚{} 小和尚{}'.format(Result[0],Result[1]))
#上一行：返回的是个元组 元组是可以通过索引去取值的

#3. 指定一个列表 列表里含有唯一一个只出现过一次的数字 写程序找出这个“独一无二”的数字
#重复----去重问题----集合Set
list1=[1,3,44,22,22,66,3,66,44,44,44,44]
set1=set(list1)
# print(set1)
for i in set1:
    list1.remove(i)
set2=set(list1)
# set3=set1 - set2
# print(set3)     #这三行的方法 找出的是Set的形式
for i in set1:
    if i not in set2:
        print(i)




