#tell  文件定位  返回指针当前所在位置    使用于读写文件时
# with open('Text03.txt','r',encoding='utf-8') as f:
#     print(f.read(3))
#     print(f.tell()) #输出“7”    utf-8 汉字占三个字节
#     print(f.read(2))
#     print(f.tell())

#truncate 可以对源文件进行截取操作
# fobjB=open('Text03.txt','r')
# print(fobjB.read())
# fobjB.close()
# print('截取之后的数据:')
# fobjA=open('Text03.txt','r+')
# fobjA.truncate(7)   #保留前5个字符
# print(fobjA.read())
# fobjA.close()

#seek() 控制光标所在位置
fobj=open('./Test04.txt','w')   #建立一个新的文本
fobj.write('DasisteinTest.') #写入信息
fobj.close()                    #关闭

with open('Test04.txt','rb') as f:  #r:数字表示字符数 #b+:数字表示字节数
    data=f.read(2)              #读取2个字节
    # print(data.decode('utf-8')) #将二进制解码成utf-8形式
    # f.seek(-2,1)                #后标志为1表示以当前开始  -2相当于光标左移两个字节 又设置到了0的位置
    # print(f.read(4).decode('utf-8'))
    # f.seek(-6,2)                #后标志为2表示以末尾开始
    # print(f.read(6).decode('utf-8'))
    f.seek(4,0)                 #后标志为0表示光标从0的位置开始 向右移动4个字节
    print(f.read(4).decode('utf-8'))

#对于这种情况 用'r'模式打开文件 而不使用二进制选项打开文件 则只允许从文件开头计算相对位置
#若从文件尾部计算或从文件当前计算 则异常


