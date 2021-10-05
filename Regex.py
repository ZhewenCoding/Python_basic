#正则表达式  通过re模块学习使用
#re.match方法 尝试从字符串的起始位置匹配一个规则 匹配成功就返回match对象 否则返回None
#可以使用group()获取匹配成功的字符串 如果匹配失败会报错 因为此时re.match返回None空对象
#仅能从起始位置匹配 中间的不算
#group() 如果有多个匹配结果的话 会以元组的形式 存放到group对象中 此时可以通过下标去获取
# import re
# data='Python is the best language in the world.'
# result=re.match('Py',data)   #精确匹配
# #语法: re.match(pattern,string,flags=0)
# print(type(result))     #返回<class 're.Match'>
# print(result.group())

import re
data='Python is the best language in the world.'
result=re.match('pYtH',data,re.I)     #re.I:忽略大小写
print(result)
print(result.group())

