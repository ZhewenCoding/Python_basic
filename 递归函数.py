#求阶乘
#用循环的方式：
# def factorial1(n):
#     for item in range(1,n+1):
#         result=1
#         for item in range(1,n+1):
#             result*=item
#         return result
#
# print('10的阶乘{}'.format(factorial1(10)))

#用递归的方式：
# def factorial2(n):
#     if n == 1:
#         return 1
#     else:
#         return  n*factorial2(n-1)
#
# print('5的阶乘{}'.format(factorial2(5)))
#递归满足的条件：
#自己调用自己
#必须有一个明确的结束条件
#优点：逻辑简单 定义简单
#缺点：容易导致栈溢出 内存紧张 甚至内存泄漏

#递归案例 模拟实现 树形结构的遍历
import os #引入文件操作模块
def findFile(file_Path):
    listRs=os.listdir(file_Path)  #得到该路径下所有的文件和文件夹
    for fileItem in listRs:
        full_path=os.path.join(file_Path,fileItem)  #获取完整的文件路径
        if os.path.isdir(full_path): #判断是否是文件夹
            findFile(full_path) #如果是一个文件夹 再次去递归
        else:
            print(fileItem)

    else:
        return

#调用搜索文件夹对象
findFile('C:\\360驱动大师目录\驱动备份目录')
