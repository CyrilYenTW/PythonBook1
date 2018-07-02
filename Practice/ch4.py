'''
4-1 比萨 ：
'''
# 想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
flavors = ['夏威夷', '義式經典', '素食']
for flavor in flavors:
	print(flavor)

# 修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
frefix = '我喜歡吃 '
suffix = ' Pizza'
for flavor in flavors:
	print(frefix + flavor + suffix)

# 在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
frefix = '我喜歡吃 '
suffix = ' Pizza'
for flavor in flavors:
	print(frefix + flavor + suffix)

print('只要是 Pizza 我都喜歡')


'''
4-2 动物 ：
'''
# 想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
animals = ['Cat', 'Dog', 'Pig']

for animal in animals:
	print(animal)

# 修改这个程序，使其针对每种动物都打印一个句子，如“Adogwould makea great pet”。
for animal in animals:
	print(animal + 'is animal.')

# 在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any oftheseanimals would makea great pet!”这样的句子。
for animal in animals:
	print(animal + 'is animal.')

print('They are cut.')


'''
4-3 数到20 ：使用一个for 循环打印数字1~20（含）。
'''
for num in range(1, 21):
	print(num)


'''
4-4 一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl+ C停止输出，或关闭输出窗口）。
'''
for num in list(range(1, 10**6+1)):
	print(num)
	break # 先跳掉



'''
4-5 计算1~1 000 000的总和 ：
'''
# 创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的
digits = list(range(1, 10**6+1))
print('min => ' + str(min(digits)))
print('max => ' + str(max(digits)))
print('len => ' + str(len(digits)))

# 调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
print('sum => ' + str(sum(digits)))

'''
4-6 奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
'''
'''
4-7 3的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
4-8 立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循
环将这些立方数都打印出来。
4-9 立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方。

'''
