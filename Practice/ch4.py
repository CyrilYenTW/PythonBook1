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

