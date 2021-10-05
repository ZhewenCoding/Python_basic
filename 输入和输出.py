#输出 %占位符
# Name='Wugui Ben'
# Uni='Stuttgart'
# Alt=25
# print('Ich heisse %s, bin schon %d und studiere an der Uni. [%s].'%(Name,Alt,Uni))
# print('-Kann ich eine neue Zeile haben? \n-Aber natuerlich!')
# print('Lass und einen Stapel verwirklichen! ')
# Daten01=[(0,0,0,0),(1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4),(5,5,5,5)]
# for (a,b,c,d) in Daten01:
#     print(f'a={a}  b={b}  c={c}  d={d}\na+1={a+1} b+1={b+1} c+1={c+1} d+1={d+1}')
#-------------------------------------------
#编码完成下面名片的显示：
# Name='老夫子'
# QQ=66666666       #或String
# Tele=11257236262  #或String
# Addr='深圳市龙岗新区'
# # print('=============================')
# # print('姓名：%s\nQQ:%d\n手机号：%d\n公司地址：%s'%(Name,QQ,Tele,Addr))
# # print('=============================')
# #或者分开写：
# # print('=============================')
# # print('姓名：%s'%Name)
# # print('QQ:%d'%QQ)
# # print('手机号：%d'%Tele)
# # print('公司地址：%s'%Addr)
# # print('=============================')
# #格式化输出的另一种方式：{} (要用花括号！).format()
# print('=============================')
# print('姓名：{}'.format(Name))
# print('QQ:{}'.format(QQ))
# print('手机号：{}'.format(Tele))
# print('公司地址：{}'.format(Addr))
# print('=============================')
# #添加参数：
# PLZ=19678
# print('公司地址：{}\n邮编：{}'.format(Addr,PLZ))


#-----------------------------------------
#上面是输出，接下来是输入：input方法的练习   注意：input只能输入str类型，不能输入数字类型！！！
# Name=input("请输入您的姓名：")
# QQ=input("请输入您的QQ号")
# Tele=11257236262
# Addr='深圳市龙岗新区'
# print('姓名：%s\nQQ:%s\n手机号：%d\n公司地址：%s'%(Name,QQ,Tele,Addr))
#-----------------------------------------
#自己做一个有意思的：
#顺便加入while循环,最多允许查询5次成绩：
i=4
while i>-1:
    MatrikelNummer=int(input("Bitte Ihre Matrikelnummer eintippen:"))
    if MatrikelNummer>=0 and MatrikelNummer<=9999999:
        print("Bitte warten darauf...")
        Entscheidung = int(input("Wollen Sie Ihre Noten wirklich sehen?  [Ja--1/Nein--0]: "))
        if Entscheidung > 0:
            print("Ihre Noten dieses Semesters sind:\n")
            print("=========================================")
            print("Automatisierungstechnik: 1.3\nRegelungstechnik: 1.5\nFachpraktikum: 2.0")
            print("=========================================")
            print("Die waren nicht so schlecht, also gib Gas in neuem Semester!")
            if i != 0:
                print("Sie haben noch %d Mal Chancen,um die Maschine zu benutzen. " % (i))
            else:
                print("Sie haben schon insgesamt 5 Mal versucht, die Maschine ist jetzt sperrt.")
                print("Um die Maschine weiterzubenutzen, bitte ruf den Administrator an. ")
        else:
            print("es scheint, dass Sie sich selbst nicht vertrauen...")
            if i != 0:
                print("Sie haben noch %d Mal Chancen,um die Maschine zu benutzen. " % (i))
            else:
                print("Sie haben schon insgesamt 5 Mal versucht, die Maschine ist jetzt sperrt.")
                print("Um die Maschine weiterzubenutzen, bitte ruf den Administrator an. ")
    else:
        print("Ihre Matrikelnummer ist nicht korrekt!")
        if i != 0:
            print("Sie haben noch %d Mal Chancen,um die Maschine zu benutzen. " % (i))
        else:
            print("Sie haben schon insgesamt 5 Mal versucht, die Maschine ist jetzt sperrt.")
            print("Um die Maschine weiterzubenutzen, bitte ruf den Administrator an. ")
    i-=1
# print("Sie haben schon insgesamt 5 Mal versucht, die Maschine ist jetzt sperrt.")
# print("Um die Maschine weiterzubenutzen, bitte ruf den Administrator an. ")
#对input做强制由str转换成其他类型：
# Name=input("请输入您的姓名：")
# Age=int(input("请输入您的年龄："))   #这里进行强制转换成了int型
# QQ=input("请输入您的QQ号：")
# Tele=11257236262
# Addr='深圳市龙岗新区'
# print('姓名:%s\n年龄:%d\nQQ号码:%s\n电话号码:%s\n公司地址:%s'%(Name,Age,QQ,Tele,Addr))
