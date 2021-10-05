#字符串操作
# Test='python'
# print(type(Test))
# print('获取第一个字符:%s'%Test[0])
# print('获取第二个字符:%s'%Test[1])
# for item in Test:
#     print(item,end=' ')

# name='peter'
# print('姓名首字母转换成大写为：%s'%name.capitalize())
#
# a='    Hi im Gui        '
# print('清除字符串左右两侧空格为：%s'%a.strip())   #只能清除左右两侧空格
# print('清除字符串左边空格为：%s'%a.lstrip())
# print('清除字符串右边空格为：%s'%a.rstrip())
#
# #复制字符串：
# print('a的内存地址%d'%id(a))    #id函数 可以查看一个对象的内存地址
# b=a #在此只是把a对象的内存地址赋给了b
# print('b的内存地址%d'%id(b))
# print(b)
#
# dataStr='Ich liebe Python!'
# print(dataStr.find('Py'))  #可以查找目标对象再序列对象中的(首个)位置 找不到会返回-1
# print(dataStr.index('P')) #同样检测字符串中是否包含子字符串 返回的是下标值 找不到会报错
# print(dataStr.startswith('I'))
# print(dataStr.endswith('!'))
# print(dataStr.lower()) #全转换成小写
# print(dataStr.upper()) #全转换成大写
#
# #切片操作：
# strMsg='Hello World!'
# #slice[start:end:step]    左闭右开 start <= value < end 范围
# print(strMsg[2:8])
# print(strMsg[2:])  #输出从第三个字符到最后
# print(strMsg[0:3])   #可以省略0，变成下面的写法：
# print(strMsg[:3])
# print(strMsg[::-1]) #倒序输出 负号表示方向 从右向左去遍历

#-------------------------------------------------------------------
#列表list
# li=[] #空列表
# li=[1,2,3,'你好']
# print(len(li))   #len函数可以获取list的长度（即列表中的对象个数）
# #对比：
# strA='Ich liebe Python!'
# print(len(strA)) #这里len函数获取字符串的长度
#
# #list中的查找
listA=['abc',765,12.23,'qiqi',True]
# print(listA) #输出完整的列表
# print(listA[3]) #输出第一个元素
# #list切片：
# print(listA[1:3]) #输出从第二个开始到第三个元素
# print(listA[2:]) #输出从第三个开始到最后所有元素
# print(listA[::-1]) #负数 从右向左倒序输出
#
# print(listA*3) #输出多次列表中的数据【复制】

# #追加：
# print('追加之前',listA)
# listA.append(['fff','ddd',233])
listA.append([11,22,33,44])
print('追加之后',listA) #追加之后相当于list嵌套
#
# #插入：
# listA.insert(1,'新的数据') #前面表示插入位置 后面表插入内容
# print(listA)
#
# rsData=list(range(10)) #强制转换为list对象
# listA.extend(rsData) #扩展 等于批量增加
listA.extend([11,22,33,44]) #效果跟上一行一样
print(listA)
#
# #修改：    不需要调用新的函数
# print('修改之前',listA)
# listA[0]='peter'
# listA[1]=0.02
# print('修改之后',listA)

#删除list数据项
# listB=list(range(10,50))
# print(listB)
# del listB[0] #删除列表中第1个元素
# print(listB)
# del listB[1:3] #批量删除多项数据 slice
# print(listB)
#del listB[0,2]   #这个是错误的！

# listB.remove(15) #移除指定的元素（15是具体数据值，不是索引值“第15个”）
# print(listB)
# listB.pop(2) #移除指定的项，2是索引值，不是具体数据值
# print(listB)
#
# print(listB.index(19))  #返回的是一个索引下标
# print(listB.index(19,20,25))
#↑ 19：要查找的具体数据值 20：从第20个数据（索引值）开始查找 25：到第25个数据（索引值）结束

#----------------------------------------------------------------------
#元组
#tupleA=() #空元组
# tupleA=('abc',89,3.14,'peter',[11,22,33])    #[11,22,33]只算作一个数据
# print(tupleA)

#查询
# for item in tupleA:
#     print(item,end=' ')
# print(tupleA[2])
# print(tupleA[2:4])
# print(tupleA[::-1])
# print(tupleA[::-2])   #表示反转字符串，每隔2个取一次
# print(tupleA[::-3])
#
# print(tupleA[-2:-1:]) #倒着取下标 为 -2 到 -1 区间的

#尝试修改元组数据：
# tupleA[0]='say hi'    #不能如此修改
# print(tupleA)    #报错

#修改tuple中的list的数据:
# print(tupleA)
# tupleA[4][0]=251515
# print(tupleA)   #可以对元组中的列表进行修改
#
# tupleB=(1,)
# tupleC=(1)    #单个数据要加逗号 否则视为整型数处理
# tupleD=('A')   #单个数据要加逗号 否则视为Str处理
# print(tupleB)
# print(type(tupleB))
# print(type(tupleC))
# print(type(tupleD))
#
# print(type(range(10)))
# print(range(10))
#
# tupleE=tuple(range(10))   #强制转换成元组类型
# print(tupleE)
# print(tupleE.count(8))  #计数 在tupleE中出现了多少次数据8

#--------------------------------------------------------------
#dict字典
# dictA={} #空字典
dictA={'pro':'艺术','school':'北京电影学院'}
# #添加字典数据：
# dictA['name']='李易峰' #左边为key，右边为value
# dictA['age']=30
# dictA['pos']='歌手'
# # #结束添加
# print(dictA)    #输出完整的字典
# print(len(dictA))  #数据项长度，以逗号分隔来计数
#
# #查找：
# print(dictA['name'])  #通过键获取对应的值
#
# #修改键对应的值：
# dictA['name']='王力宏'
# dictA['school']='伯克利音乐学院'
# print(dictA)
#
# #修改/添加（更新）：
# dictA.update({'weight':73.0})
# print(dictA)
#
# #删除 用del 或pop
# del dictA['name']
# print(dictA)
# dictA.pop('age')
# print(dictA)


# #获取所有的键：
# # print(dictA.keys())
print('全体键为：',dictA.keys())
#
# #获取所有的值：
# # print(dictA.values())
print('全体值为：',dictA.values())
#
# #获取所有的键值对：
# # print(dictA.items())
print('全体键值对为：',dictA.items())
#
# #获取所有的键和值：
for key,value in dictA.items():
    # print(key,'--',value)
    # print(value)
    print('%s==%s'%(key,value))

#字典排序 按照key排序
# print(sorted(dictA.items(),key=lambda d:d[0]))

#字典排序 按照value排序
# print(sorted(dictA.items(),key=lambda d:d[1]))   #将前面float改成int后不会报错