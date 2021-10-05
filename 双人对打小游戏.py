#两个人物：关羽/吕布
#属性：
#name:玩家名字
#hp:玩家血量

#方法：
#attack():普通攻击，对方-10hp
#ultimate():大招攻击，对方-20hp
#healing():打药，自己+15hp
#__str__打印玩家状态

#第一步：定义一个类【角色类】
# import time #导入时间的包
# class Role:
#     def __init__(self,name,hp):
#         '''
#         构造初始化函数
#         :param name:    角色名
#         :param hp:      血量
#         '''
#         self.name=name
#         self.hp=hp
#
#     def attack(self,enemy):
#         enemy.hp-=10
#         info='【%s】对【%s】触发了普通攻击'%(self.name,enemy.name)
#         print(info)
#
#     def ultimte(self,enemy):
#         enemy.hp-=20
#         info='【%s】对【%s】触发了大招攻击'% (self.name,enemy.name)
#         print(info)
#     def healing(self):
#         self.hp+=15
#         info='【%s】使用了长生丸  hp+15'%(self.name)
#         print(info)
#     def __str__(self):
#         return '【%s】剩余 %s 血量'%(self.name,self.hp)
#
# #创建两个实例化对象——【关羽】 【吕布】
# gy=Role('关羽',100)
# lb=Role('吕布',105)
# #使之自动跑起来——加while循环
# while True:
#     if gy.hp <= 0 or lb.hp <= 0:
#         break
#     else:
#         gy.attack(lb)   #关羽对吕布 普通攻击
#         print(gy)   #打印对象状态
#         print(lb)
#         print('******************************')
#         lb.attack(gy)
#         print(gy)
#         print(lb)
#         print('******************************')
#         gy.healing()
#         print(gy)
#         print(lb)
#         print('******************************')
#         time.sleep(3)   #休眠/暂停3秒钟
# print('对战结束...')


#重写一遍 双人对战小游戏 增强熟练度：
#两个对象：  关羽    吕布
#类属性：    name   hp
#类函数（方法）：普通攻击   大招攻击    打药
import time
class StreetFight(object):
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def BasicAttack(self,enemy):
        enemy.hp-=10
        print('【%s】对【%s】发动了 普通攻击'%(self.name,enemy.name))
    def Ultimate(self,enemy):
        enemy.hp-=30
        print('【%s】对【%s】发动了 终极攻击'%(self.name,enemy.name))
    def Healing(self):
        self.hp+=15
        print('【%s】使用了  还魂丹  道具'%self.name)
    def __str__(self):
        # if self.hp >= 100:
        #     return '所选武将为：【%s】初始生命值为：【%d】'%(self.name,self.hp)
        # else:
        return '【%s】当前血量 %d'%(self.name,self.hp)

gy=StreetFight('关羽',100)
lb=StreetFight('吕布',125)
print('*'*20,'对战开始','*'*20)
while True:
    if gy.hp <=0 or lb.hp <=0:
        break
    else:
        print(gy)
        print(lb)
        gy.Ultimate(lb)
        print(gy)
        print(lb)
        lb.BasicAttack(gy)
        print(gy)
        print(lb)
        gy.Healing()
        print(gy)
        print(lb)
        time.sleep(3)
print('对战结束')
# if gy.hp <= 0:
#     print('对战结束，胜者为：【%s】' %gy.name)
# elif lb.hp <=0:
#     print('对战结束，胜者为：【%s】' %lb.name)


