# functions_names=['Charging', 'DriveIdle', 'DriveFull', 'PickItem', 'DiscardItem']
# #
# charging = {'Charger', 'ChargerCtrl', 'CPU', 'Battery', 'BatteryCtrl'}
# drive_idle = {'Camera', 'CPU', 'Battery', 'BatteryCtrl', 'U/S_Sesnor', 'MotorCtrl', 'Hall_Sensor', 'Motors', 'Wheels'}
# drive_full = {'Camera', 'CPU', 'Battery', 'BatteryCtrl', 'U/S_Sesnor', 'MotorCtrl', 'Hall_Sensor', 'Motors', 'Wheels'}
# pick_item = {'Camera', 'CPU', 'Battery', 'BatteryCtrl', 'GripperMotor', 'GripperCtrl'}
# discard_item = {'Camera', 'CPU', 'Battery', 'BatteryCtrl', 'GripperMotor', 'GripperCtrl'}
# #
# functions_components = [charging, drive_idle, drive_full, pick_item, discard_item]

# print(functions_names)
# print(functions_components)
# print(functions_components[3])

# print(drive_idle.union(pick_item))  #求并集
# print(drive_idle.intersection(pick_item))   #求交集
# print(drive_idle.difference(pick_item))     #前者和后者的差别 只输出前者具有的/后者不具有的
# print(drive_idle.symmetric_difference(pick_item))   #双方彼此不共同具有的 全部输出

#加入dict功能    格式 —— (key)功能名：(value)对应元器件
functions_dict = {
    'Charging': {'Charger', 'CPU', 'ChargerCtrl', 'Battery', 'BatteryCtrl'},
    'DriveIdle': {'CPU', 'BatteryCtrl', 'Camera', 'Wheels', 'U/S_Sesnor', 'Battery', 'MotorCtrl', 'Motors', 'Hall_Sensor'},
    'DriveFull': {'CPU', 'BatteryCtrl', 'Camera', 'Wheels', 'U/S_Sesnor', 'Battery', 'MotorCtrl', 'Motors', 'Hall_Sensor'},
    'PickItem' : {'Camera', 'CPU', 'Battery', 'BatteryCtrl', 'GripperMotor', 'GripperCtrl'},
    'DiscardItem' : {'Camera', 'CPU', 'Battery', 'BatteryCtrl', 'GripperMotor', 'GripperCtrl'},
}

# print(functions_dict) #优点 输出时有对应函数名作为参考
# print(functions_dict['PickItem'])
# print(zip(functions_names, functions_components))
# print(list(zip(functions_names, functions_components)))   #打包成list 对象被打包成list中的tuple

# functions_dict = dict(zip(functions_names, functions_components))   #打包成dict
# print(functions_dict)
# print(functions_dict['PickItem'])

#dict 将key和value互换： (key)元器件：(value)对应功能名
# components_names = {component for components in functions_dict.values() for component in components}
#为什么 for 前面加 component ?   为什么连续用两个for？
# print(components_names)
# import random
# components_status = {component:random.choices(['Broken', 'Functioning'], [0.3, 0.7])[0] for component in components_names};
# print(components_status)


#测试random及其choice：
import random
print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))   #随机生成一个数
# print("choice([1, 2]) : ", random.choice(['a', 'b'],[0.5,0.5]))
# 报错 choice() takes 2 positional arguments but 3 were given

# print("choice('A String') : ", random.choice('abcde'))


#zip小例子：
#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
# a=[1,2,3]
# b=['a','b','c']
# zipped0=list(zip(a,b))   #Python 3.x 如需展示列表，需手动 list() 转换
# zipped1=dict(zip(a,b))
# zipped2=tuple(zip(a,b))
# zipped3=zip(a,b)
# print(zipped0)      #[(1, 'a'), (2, 'b'), (3, 'c')]
# print(zipped1)      #{1: 'a', 2: 'b', 3: 'c'}
# print(zipped2)      #((1, 'a'), (2, 'b'), (3, 'c'))
# print(zipped3)      #<zip object at 0x000001887FF86D80>
