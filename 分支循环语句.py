# score=50
# if score<=60:
#     print("成绩不够理想，要继续加油噢！")
#     pass   #空语句
# print("语句运行结束")
#-------------------------------------
#尝试改变score=50成input()
# score=int(input("请输入成绩："))
# if score<=60:
#     print("成绩不够理想，要继续加油噢！")
#     # pass   #空语句
# # print("语句运行结束")
# else:
#     print("恭喜恭喜，顺利通过考试!")
#     # pass

#写一个elif的例子：
# score=int(input("请输入成绩："))
# # print(type(score))
# if score>100:
#     print("扯犊子呢")
# elif score>90:
#     print("您的成绩是A等级，真不戳")
# elif score>=80:
#     print("您的成绩为B等级")
# elif score>=70:
#     print("您的成绩为C等级")
# elif score>=60:
#     print("您的成绩为D等级")
# else:
#     print("啊这...")
# print("程序运行结束")

#----------------------------
#人机划拳小游戏（多分支练习）
#石头0 剪刀1 布2
# import random
# inp = int(input('请出拳：石头0 剪刀1 布2'))
# computer = random,randint(0,2)
# print('电脑出拳:%d'%computer)
# if inp > 2:
#     print('输入错误')
# elif inp == 0 and computer == 2:
#     print('厉害了，居然赢了')
# elif inp == 1 and computer == 0:
#     print('厉害了，居然赢了')
# elif inp == 2 and computer == 1:
#     print('厉害了，居然赢了')
# elif inp == computer:
#     print('不错，居然打成平手')
# else:
#     print('哈哈，输了吧')
#问题报错：randint未定义；是否有random包？

#if-else的嵌套使用：
# LP=int(input("请输入学分"))
# if LP >= 10:
#     Note = int(input("请输入成绩"))
#     if Note>=160:
#         print("您可以申请该实习岗位")
#     else:
#         print("您需要继续提高平均成绩才可以申请")
# else:
#     print("抱歉，您不符合申请条件")

# print(1)
# print(type(1))
# print("1")
# print(type("1"))
# print((1))
# print(type((1)))
# print([1])
# print(type([1]))
# print({1:1})
# print(type({1:1}))

#循环语句：  while / for

#1.输出1--100的数据
# index=1
# while index<=100:
#     print(index)
#     index+=1

# i=0
# while i<5:
#     print('第%d次循环：'%i)
#     print('i=%d'%i)
#     i+=1

#打印99乘法表：
# row=1
# while row<=9:
#     col=1
#     while col<=row:
#         print("%d*%d=%d"%(row,col,row*col),end=" ")
#         col+=1
#     print()
#     row+=1

#打印直角三角形：
# row=1
# while row<=7:
#     j=1
#     while j<=row:
#         print('*',end=" ")
#         j+=1
#     print()
#     row+=1

#等腰三角形：
# row=1
# while row<=5:
#     j=1
#     while j<=5-row:
#         print(' ',end='')
#         j+=1
#     k=1
#     while k<=2*row-1:
#         print('*',end='')
#         k+=1
#     print()
#     row+=1

#for循环：
# tags='Ich bin Wugui Ben'
# for items in tags:
#     print(items,end='')

#for循环+range函数：
# sum=0
# for data in range(1,101):  #range 左包含右不包含
#     sum+=data
#     print(data,end=' ')
# print()
# print('和为：%d'%sum)

#输出所有偶数：
# for data in range(1,201):
#     if data%2 == 0:
#         if data <=101:
#             print(data,end=(' '))

#测试continue和break:
# for data in range(1,201):
#     if data % 2 == 0:
#         continue    #使148行被跳过
#         print('本条不会显示')
#     print('所有奇数为：%d'%data)

# for words in 'Ich liebe Python!':
#     if words == 'b':
#         break
#     print(words,end='')

# for words in 'Ich liebe Python!':
#     if words == 'o':
#         continue
#     print(words,end='')
#---------------------------------
# index=1
# while index<=100:
#     if index>20:
#         print('超过了规定值,结束导出')
#         break
#
#     print('号码为：%d'%index)
#     index+=1

#99乘法表用for来实现：
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end=' ')
#     print()

#break的作用域：
# for item in range(1,11):
#     print(item,end=' ')
#     if item >= 5:
#         break
# else:
#     print('在上面的循环中 只要出现了break 那么else的代码将不再执行')

#写一个登陆程序，三次输入错误账号密码则锁定系统：
#为了避免最后一次尝试失败后出现“请重试”的提示，在验证账号密码时多加一个i<2的条件。
#登陆成功后用break直接退出循环，下面的else不会被执行。
# account='wugui'
# password='12345'
#
# for i in range(3):
#     zh = input('请输入您的哔哩哔哩账号(区分大小写及空格)：')
#     mm = input('请输入您的哔哩哔哩密码(区分大小写及空格)：')
#     if (zh != account or mm != password) and i < 2 :
#         print('用户名或密码错误，请重试')
#
#     elif zh == account and mm == password:
#         print('登陆成功，正在加载主站页面...')
#         break
# else:
#     print('您已被限制登录，请联系哔哩哔哩客服')

#写一个猜年龄小游戏，要求如下：
#1.允许用户最多尝试3次
#2.每尝试3次后，如果还没猜对，问用户是否还想继续玩（Y 或 N）
#回复Y则继续往复，回复N则退出程序
#3.如果猜对了，显示恭喜，并退出程序

#自己的思路:a.暂时不用随机数函数，自定义一个年龄  b.用range函数代替自增
#玩家用input函数键入猜测的年龄值
# age=25
# try_times=0
# while try_times != -1:
#     for i in range(3):
#         gamer=int(input('请输入您猜测的年龄：'))
#         if gamer != age:
#             print('您的猜测不正确噢，请重新猜测~')
#         else:
#             print('恭喜您猜对啦，请私信up主领奖！')
#             break
#     else:
#         decision=input('您的3次机会已用尽，是否继续下一轮？[Y--继续 / N--结束游戏]')
#         if decision == 'Y' or 'y':
#             try_times +=1
#             continue
#         elif decision == 'N' or 'n':
#             print('您一共重试了%d轮'%try_times)
#             print('感谢您的参与，下次见!')
#             break
#         # elif decision != 'Y' or 'N':
#         #     print('请输入Y或N！')
# #！！！！！！
# #问题（229，230）：如果输入了非Y非N的值，怎么跳转到让继续输入Y或N？
#     if gamer == age:
#         break
    # try_times+=1

#这里做了手脚，不是无限次的刷新机会，而是有限次（设置的为100次）
#那 怎么让它可以无限循环呢？
#按这个逻辑，可以设置一个使得while永远成立的条件，这里我用了个非负数不等于-1，另外可以再实现个计数功能。
#即“该玩家一共重玩了多少轮”。

#视频给出的参考程序：
# times=0
# count=3
# while times<=3:
#     age=int(input('请输入您要猜的年龄'))
#     if age == 25:
#         print('恭喜猜对了')
#         break
#     elif age > 25:
#         print('猜大了，请再试试')
#     else:
#         print('猜小了，请再试试')
#     times+=1
#     if times == 3:
#         choose=input('想不想继续猜呢？Y/N')
#         if choose == 'Y' or choose == 'y':
#             times=0 #重置为初始值
#         elif choose == 'N' or choose == 'n':
#             times=4
#             print('游戏结束')
#         else:
#             print('请输入正确的标记，谢谢配合')

#----------------------------------------------------------
#练习：小王身高1.75m，体重80.5kg，根据BMI公式计算BMI指数
#根据BMI指数（if elif）判断并打印结果

#思考：input输入身高和体重

# Height=float(input('请输入您的身高（单位为m）'))
# Weight=float(input('请输入您的体重（单位为kg）'))
# BMI=Weight/Height**2
# print('经计算，您的BMI指数为：%f'%BMI)
# if BMI < 18.5:
#     print("您体重过轻，记得多吃肉")
# elif BMI >= 18.5 and BMI < 25:
#     print('您身体一切正常')
# elif BMI >= 25 and BMI < 28:
#     print('您体重过重，请注意饮食')
# elif BMI >= 28 and BMI < 32:
#     print('您属于肥胖人群，请严格注意饮食')
# elif BMI >=32:
#     print('您已严重肥胖，请立即减肥')
