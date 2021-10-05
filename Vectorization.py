import numpy as np
# a = np.array([1,2,3,4])
# print(a)

import time #计算需要的时间

a = np.random.rand(1000000)
#以给定的形状创建一个数组 并在数组中加入在[0,1]之间均匀分布的随机样本
#给定的形状 指的是 rand(a,b) 生成一个a*b的数组（矩阵） 本例为一个1000000*1的 列向量
b = np.random.rand(1000000)

tic = time.time()  #返回当前时间的时间戳（1970纪元后经过的浮点秒数）
c = np.dot(a,b)
toc = time.time()

print(c)
print('Vectorized version:' + str(1000*(toc-tic)) + 'ms') #秒转化为毫秒

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print('For loop:' + str(1000*(toc-tic)) + 'ms')

#结果 向量化后代码相比for循环运行快接近300倍
