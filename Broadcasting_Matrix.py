import numpy as np
# #
# A = np.array([[56.0,0.0,4.4,68.0],
#              [1.2,104.0,52.0,8.0],
#              [1.8,135.0,99.0,0.9]])
# print(A.shape)      #查看A数组的维度  结果：(3,4)
# # print(A)
# cal = A.sum(axis=0)     #axis=0 竖直相加    axis=1 水平相加  结果都是1*m型矩阵
# print(cal)
# # percentage  100*A/(cal.reshape(1,4))     #先reshape cal 转换成需要的矩阵格式再相除
# percentage= 100*A/cal                    #这里 不需要reshape也能正确输出
#                                          #调用的目的是 当不知道cal是什么矩阵时 确保cal转换正确
#                                          #reshape是o(1)操作 成本很低
# print(percentage)

#Python向量的说明：
# import numpy as np
# a1 = np.random.rand(4,4)#返回“0~1”均匀分布随机样本矩阵(4*4)
# a = np.random.randn(5)  #返回5个标准正态分布N(0,1)随机样本 即随机高斯变量 为数组形式 非矩阵
                        #Dont use rank 1 array like this!
# a = a.reshape(5,1)      #可以通过reshape将a数组转换成(5,1)型矩阵
# b = np.random.randn(5,3)    #5*1型随机数矩阵 为矩阵 非数组
                        #Use this(matrix)!
# print('a:',a)     #a: [ 0.91661784 -0.30903122 -0.00279358 -0.44049721  0.36397878]
#                   #秩为1的数组 array
# print('b:',b)     #b: [[-0.07245008 -0.41373789 -2.80643439  0.60326427  2.57315227]]
# print('a shape:',a.shape)          #结果为(5,)
# print('b shape:',b.shape)
# print('a.T:',a.T)              #转置和非转置相同
# print('b.T:',b.T)              #矩阵转置  正常转置
# print('a.dot:',np.dot(a,a.T))  #内积  输出为一个数字
# print('b.dot:',np.dot(b,b.T))  #5*5型矩阵
# assert (a.shape == (5,))    #assertion 断言 确保括号内条件满足 不满足会报错
# assert (b.shape == (1,5)),'b矩阵不是(1,5)型矩阵！'

#测试Dropout regularization (S18)
# keep_prob = 0.8
# a1 = np.random.rand(4,2)
# # print('a1:',a1)
# print(a1.shape[0])      #读a1有多少行(4行)
# print(a1.shape[1])      #读a1有多少列(2列)
# a3 = np.ones((4,4))
# d3 = np.random.rand(a3.shape[0],a3.shape[1]) < keep_prob   #d3用来决定(随机决定)第三层中哪些单元归零
# print('d3:',d3)             #True = 1   False = 0    1和0可参与运算
# a3 = np.multiply(a3,d3)     #矩阵按元素相乘  去掉了a3中对应b3随机生成的 >= 0.8的元素的位置的元素
# print('a3:',a3)             #实现了按给定概率随机删除节点的效果
# a3 /= keep_prob
# print(a3)

#测试判断大小后输出矩阵 测试multiply
# prob = 0.5
# x = np.random.rand(4,4)
# print('x:',x)
# y = x < prob
# print('y:',y)
# z = np.multiply(x,y)
# print('z:',z)

#Weight initialization  (S21)  权重初始化
w_3 = np.random.randn((3,2)) * np.sqrt(1 / n_2)

#测试np.sqrt  按元素开根号
# x = np.array([[1,2,3],[3,2,1]])
# y = np.sqrt(x)
# print(y)

