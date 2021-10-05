#常用的匹配规则
# . 点的使用    匹配规则:除了换行符之外所有字符
import re
# data='aeiou'
# names='小张','小王','小孙'
# pattern0='小.'   #匹配规则
# pattern='..'     #匹配规则
# for name in names:
#     res=re.match(pattern0,name)
#     if res:
#         print(res.group())

#[]中括号的使用  匹配规则:匹配中括号中的任意一个字符
# str1='eHllo'
# res=re.match('[eH]',str1)
# if res:
#     print(res.group())
# pattern='[abc]' #使用中括号括起来的内容 代表一个集合 代表匹配集合中的任意一个字符
# pattern='[a-z]'     #"-"可以扩大范围  "到"
# #[abc]代表可以匹配a或b或c
# dataset0='a','b','c','e','wyw','cc'
# for data in dataset0:
#     result=re.match(pattern,data)
#     if result:
#         print('匹配成功%s'%result.group())

#\d匹配一个数字 0-9
# data='Aa72345abcdef'
# print(re.match('\d',data).group())
# print(re.match('\d\d',data).group())    #可叠加

#\D匹配一个非数字
# print(re.match('\D\D',data).group())

#\s匹配一个空白字符 或者tab键
# data='  XXR'
# print(re.match('\s',data).group())

#\S匹配非空白字符
# data='$  '
# print(re.match('\S',data).group())

#\w匹配单词字符 a-z A-Z 0-9 _
# data='S_sgga11$'
# print(re.match('\w\w',data).group())

#\W匹配非单词的字符
# data=' ^%1145f'
# print(re.match('\W\W',data).group())

#*匹配前一个字符出现0次或者无限次 即可有可无
# res=re.match('[A-Z][A-Z]*','My')  #匹配0次
# res=re.match('[A-Z][a-z]*','My')    #匹配2次
# res=re.match('[A-Z][a-z]*','Mybb')  #匹配3次
res=re.match('[A-Z][a-z]*','MyloveIsgone')
print(res.group())
