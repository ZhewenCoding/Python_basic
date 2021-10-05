#Set不支持切片和索引 是一个无序的且不重复的容器
#类似于字典 但是只有key 没有value
#创建集合
# set1={1,2,3}
# set2={2,3,4}
# dict1={}
# dict2={1:3}
# print(type(set1))
# print(type(dict1))
# print(type(dict2))

#添加操作
# set1.add('python')
# print(set1)
# set1.add(5)
# print(set1)
#
# #清空操作
# set1.clear()
# print(set1)

#取差集操作  difference函数和-（减号）都可以
# set3=set1.difference(set2)
# print('diff.后',set3)
# print('无中间变量 直接输出时',set1.difference(set2))
# print('减法后',set1 - set2)
#
# #取交集操作  intersection函数和 & 都可以
# print(set1.intersection(set2))
# print(set1 & set2)
#
#取并集操作  union函数和 | 都可以    不改变原集合
# print(set1.union(set2))
# print(set1 | set2)
# print(set1)

#移除 随机(不完全随机)移除一个数据并获取该数据 用pop函数
# print(set1)
# GetRandomData=set1.pop()
# print(GetRandomData)
# print(set1)

#移除
# print(set1.discard(3))  #指定移除的元素
# print(set1)

#更新（即取并集）    会改变原集合（本例为set1）
# set1.update(set2)
# print(set1)

#测试强制转换成集合：
list1=[1,1,2,4,5,6,5]
tuple1=(1,1,2,4,5,6,5)
dict1={'a':1,'b':2,'c':3,'a':2,'b':1}
print(dict1)
set1=set(list1)
set2=set(tuple1)
set3=set(dict1)
print(set1)
print(set2)
print(set3)
#测试证实了强转方法set()可行
