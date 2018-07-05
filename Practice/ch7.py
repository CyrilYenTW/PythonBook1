'''
7-1 汽车租赁 ：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“LetmeseeifIcan find you a Subaru”。
'''
brand = input('你喜歡哪個牌子的車?')
print('我也一樣很喜歡' + brand)


'''
7-2 餐馆订位 ：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
'''
people = input('請問你幾位? ')
print( '沒有位子了' if int(people) > 8  else '請入座')


'''
7-3 10的整数倍 ：让用户输入一个数字，并指出这个数字是否是10的整数倍。
'''
num = input('請輸入10的整數倍:')
print(num + '是整數倍' if (int(num)%10 == 0) else '不是整數倍')


'''
7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨
中添加这种配料。
'''
message = ''
while message != 'quit':
	message = input('請輸入Pizza配料 : ')
	print('你輸入的是 => ' + message)


'''
7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用
户的年龄，并指出其票价。
'''
age = 99
while age > 0:
	age = int(input('請輸入您的年齡: '))
	if age < 3:
		print(' 0元')
	elif age > 13:
		print(' 15元')
	else:
		print(' 10元')


'''
7-6 三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
'''
# 在while 循环中使用条件测试来结束循环。
# 使用变量active 来控制循环结束的时机。
# 使用break 语句在用户输入'quit' 时退出循环。
active = True

while active:
	message = input('What are you say? ')

	if message == 'exit':
		print('active => False')
		active = False
	elif message == 'quit':
		print('good bye!!')
		break
	else:
		print('You say ' + message)


'''
7-7 无限循环 ：编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl+C，也可关闭显示输出的窗口）。
'''
while True:
	print('.')


'''
7-8 熟食店 ：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches 的空列表。遍历列
表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 。所有三明
治都制作好后，打印一条消息，将这些三明治列出来。
'''
sandwich_orders = ['Croque Monsieur', 'Hot Dog', 'Reuben', 'Slider', 'Sandwich Generation']
finished_sandwich = []

print(sandwich_orders)
print(finished_sandwich)

while len(sandwich_orders) > 0:
	print('I made your tuna sandwich')
	temp = sandwich_orders.pop()
	finished_sandwich.append(temp)

print(sandwich_orders)
print(finished_sandwich)


'''
7-9 五香烟熏牛肉（pastrami）卖完了 ：使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。在程序开头附近添加
这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。确认最终的列
表finished_sandwiches 中不包含'pastrami' 。
'''
sandwich_orders = ['Hot Dog', 'pastrami', 'Reuben', 'pastrami', 'pastrami', 'Slider', 'Sandwich Generation']
finished_sandwich = []

while len(sandwich_orders) > 0:
	temp = sandwich_orders.pop()
	if temp == 'pastrami':
		print('pastrami was sold out')
	else:
		print('I made your tuna sandwich')
		finished_sandwich.append(temp)

print(sandwich_orders)
print(finished_sandwich)


'''
7-10 梦想的度假胜地 ：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one placein the world, where would you go?”的提示，并编写一个打印调查
结果的代码块。
'''
places = []

while True:
	temp = input('If you could visit one placein the world, where would you go ? ')
	places.append(temp)

	if input('Do you want to exit ? (y/n) ') == 'y':
		break;

print(places)