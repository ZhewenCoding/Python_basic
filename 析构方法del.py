class Animal:
    def __init__(self,name):
        self.name=name
        print('这是构造初始化方法')
    def __del__(self):
        #主要的操作是 使对象释放 一旦对象释放完毕 该对象则不能再使用
        print('当在某个作用域下面 没有被使用【引用】的情况下 解析器会自动调用该函数 来释放内存空间')
        print('这是析构方法')
        print('%s 这个对象被彻底清理了 内存空间也释放了'%self.name)

cat=Animal('大橘')
# del cat #手动地去清理删除对象 会执行 del 函数
print(cat.name)  #此时会报错 说cat未被定义  原因是cat在上一行已被删除
# input('程序等待中... 请输入任意内容')
# dog=Animal('柯基')
