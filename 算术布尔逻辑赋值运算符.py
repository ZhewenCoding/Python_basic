# a=5
# b=7
# c=a - b
# print(c)
# print(a + c - b)
# print(a % b,a // b)
#-----------------------
# a,b=3,4
# print(f'a={a},b={b},this is the calculation result')
# print(a==b,a!=b,a>b,a<b,a>=b,a<=b)
#
# a,b='du','ich'
# print(a,b)
# print(a==b,a!=b,a>b,a<b,a>=b,a<=b)
#ASCII???
#-----------------------
#and  or  not   bitwise_AND   bitwise_OR
a,b,c,d=4,2,3,7
# print(a+b>c and d<a)
# print(a+b>c or d<a)
# print(not d>a)
print(a and b)  #布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
print(a & b)    #bitwise AND
print(a or b)   #布尔"或" - 如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值
print(a | b)    #bitwise OR

# print(d>a not)     错误
# print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and 3<2)
#-----------------------
#赋值运算符
# a,b,c,d=1,2,3,4
# a+=c
# b**=3
# c/=d
# print(a,b,c,d)
