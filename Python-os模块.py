import os
import shutil
# os.rename('Test04.txt','Text04.txt')   #重命名 前面原名 后面新名
# os.remove('ToRemove.py')               #删除
# os.mkdir('Test')                        #创建文件夹
# os.rmdir('Test')                        #删除文件夹 只能删除空目录 里面有文件则删除不了
# os.mkdir('c:/Python待删除文件夹')        #mk-"make"   只能创建一级目录
# os.rmdir('c:/Python待删除文件夹')

# os.makedirs('c:/Python待删除文件夹/第二级待删/第三级待删') #创建多级目录
# os.removedirs('c:/Python待删除文件夹/第二级待删/第三级待删')

# shutil.rmtree('c:/Python待删除文件夹')     #用来删除多级目录 哪怕里面有文件也可以删除

#获取当前目录
# print(os.getcwd())                        #结果为C:\PyCharm

#路径的拼接
# print(os.path)
# print(os.path.join(os.getcwd(),'venv'))

#获取某位置中的目录列表
# listRs=os.listdir('c:/OSMO')    #老版本的写法
# print(listRs)       #结果为整行显示 不美观
# #结果为:['17牛油果', '355856-1Z4211Q40964.jpg', '59035fb64206d.png', '60个免费....
# for dirname in listRs:  #用for循环挨个换行输出 很美观
#     print(dirname)

# rs=os.scandir('c:/OSMO')          #现代版的写法
# print(rs)
#scandir 和 with 一起使用 这样的话 上下文管理器会在迭代器遍历完成后自动释放资源
# with os.scandir('c:/OSMO') as entries:
#     for entry in entries:
#         print(entry.name)

basePath='c:/'
for entry in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath,entry)):    #只打印文件 不打印目录(文件夹)
        print(entry)
        pass
    pass


