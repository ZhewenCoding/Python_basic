#打开文件   open('文件名','打开模式')
# fobj=open('./Test.txt','w') #w为只写入模式 每次会覆盖旧内容   文件不存在将新建文件
#读/写操作
# fobj.write('测试.1')   #中文编码会报错
# fobj.write('Das ist ein Test.')
# fobj.close()
# fobj=open('./Test.txt','w',encoding='utf-8')    #加上编码utf-8后可以输入中文
# fobj.write('嘻嘻')

#以二进制形式写数据
# fobj=open('Text01.txt','wb')  #二进制模式写入
# fobj.write('晚安'.encode('utf-8'))  #encode会把字符串转换成字节类型编码
# fobj.close()

# fobj=open('Text03.txt','a',encoding='utf-8')  #a为追加
# fobj.write('测试03')  #\r回车
# fobj.write('\r晚安')  #\r回车
# fobj.write('\n早安')  #\n换行
# fobj.close()

#读数据操作
# f=open('Text03.txt','r',encoding='utf-8') #只读方式打开
# print(f.read())
# print(f.read(10))    #读取10个字符
# print(f.readline()) #读一行
# print(f.readlines())  #读所有行 返回的是列表对象
# print(f.readlines(2))   #读前2行

# f=open('Text03.txt','rb') #读取二进制 图片/视频的读取方式
# print(f.read())
# data=f.read()
# print(data)               #是二进制形式
# print(data.decode('utf-8'))      #将二进制解码成utf-8形式  （解码成gbk本机是乱码）
# f.close()   #文件对象关闭   不关闭可能卡机  用with更方便

#with上下文管理对象
#优点 程序完毕后会自动释放打开关联的对象
# with open('Text03.txt','r',encoding='utf-8') as f:
#     print(f.read())

with open('Text03.txt','a',encoding='utf-8') as f:
    f.write('Python')
    print(f.read())     #没有读权限 报错

#小结
#read: r r+ rb rb+
#r r+ 适用于普通读取
#rb rb+ 适用于文件 图片 视频 音频 文件读取
#write：w w+ wb+ wb a ab
#w wb+ w+ 每次都会创建文件
#二进制读写的时候注意编码问题
#a ab a+ 在原有的文件基础之后去文件指针的末尾追加
#并不会每次都创建新的文件



