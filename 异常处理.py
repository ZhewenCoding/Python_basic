#except在捕获错误异常的时候 是要根据具体的错误类型来捕获的
#用一个块 可以捕获多个不同类型的异常:
#Exception      当对出现的问题/错误不确定的情况下 可以使用
# try:       #不用模块的话 只能单独调试一个疑似异常的语句 因为多个的后面的不会被执行
           #无法一次排查多个异常
    # print(b)        #捕获逻辑的代码
    # li=[1,2,34]
    # print(li[4])      #通过下标去访问列表
    # a=10/0
    # pass
# except NameError as msg:    #指定了要捕获的错误类型   可以多个except
#     #捕获到的错误 才会在这里执行
#     print(msg)
#     pass
# except IndexError as msg:   #不知道就多写几种可能的错误类型
#     print(msg)
#     pass
# except ZeroDivisionError as msg:
#     print(msg)
#     pass

#---------------通吃的异常检测-----------------
# except Exception as result:
#     print(result)   #要输出才会报错    报错尽快处理掉

# print('第一次接触异常处理')
# print('第二次接触异常处理')

#异常示例（仅举几个例子）（更多参见P80  00：47）：
#IndexError     当序列的索引超出范围时引发
#NameError      在局部或全局范围内找不到变量时引发
#ZeroDivisionError      当除法或模运算的第二个操作数为零时引发

# def A(s):
#     return 10/int(s)    #s变量强转int型
#     pass
# def B(s):
#     return A(s)*2
#不需要在每个可能出错的地方去捕获 只要在合适的层次去捕获错误就可以了
#这样 大大减少写try----except的麻烦   （统一调用）
# def main2():
#     try:
#         B('0')
#         pass
#     except Exception as msg:
#         print(msg)

# main2()

#不调用Exception时 怎么阅读报错信息：
#自上而下是入口到出口的顺序 函数进入（第一行的报错信息） 下一步（第二行） 下一步（第三行）...
#就是流程正序的逻辑思路往下读

#如果在运行时发生异常 解释器会查找相应的异常捕获类型
#如果在当前函数里没有找到的话 它会将异常传递给上层的调用函数 看能否处理
#如果在最外层没有找到的话 解释器会退出 down机

#try-except-else

# try:
#     print('hi')      #语法错误不会触发Exception
#     pass
# except Exception as msg:
#     print('error:',msg)
# else:
#     print('当try里面的代码 没有出现异常的情况下 我才会执行')

#try-except-finally
# try:
#     # int('abc')
#     open('aaa.txt')        #打开文件    （没有该文件）
# except Exception as msg:
#     print(msg)
#     pass
# finally:
#     print(' 释放文件的资源 数据库连接的资源等')
#     print('----不管有没有出错都执行的代码----')

#——————————————————自定义异常————————————————————
#使用 raise 语句抛出一个指定的异常
# class TooLongException(Exception):
#     def __init__(self,leng):
#         self.len=leng
#         pass
#     def __str__(self):
#         return '您输入姓名长度是'+str(self.len)+'，超过长度了...'
#     pass
#
# def name_Test():
#     name=input('请输入姓名：')
#     try:    #添加捕获 try----except
#         if len(name) > 5:
#             raise TooLongException(len(name))
#         else:
#             print(name)
#             pass
#     except TooLongException as result:
#         print(result)
#     else:
#         print('姓名有效')
#     finally:
#         print('程序结束...')
#
# name_Test()


#自己演练一遍：
class TooLongException(Exception):
    def __init__(self,length):
        self.length=length
    def __str__(self):
        return '您输入的姓名长度为：'+str(self.length)+'，输入过长'
                                #这里为什么不强制转换str则报错？
def LengthTest():
    name=input('请输入姓名：')
    try:
        if len(name) > 5:
            raise TooLongException(len(name))
        else:
            print('名字已确认：'+name)
    except TooLongException as msg:
        print(msg)
    else:
        print('名字符合规范')
    finally:
        print('程序结束...')

LengthTest()



