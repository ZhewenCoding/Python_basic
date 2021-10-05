#------------------------------------------------
#合并操作：+
strA='今天是周六'
strB='学习Python'
print(strA+strB)
print(strA+','+strB)

listA=list(range(11))
listB=list(range(11,20))
print(listA+listB)

#------------------------------------------------
#复制操作：*
print(strA*3) #*表复制
print(listA*3)
print(5*3) #表乘以

#------------------------------------------------
#对象是否存在：in *（结果是bool值）
print('生' in strA)
print('周' in strA)
print(23 in listA)
print(15 in listB)

dictA={'age':'35','num':331}
print('age' in dictA)
print('ID' in dictA)
