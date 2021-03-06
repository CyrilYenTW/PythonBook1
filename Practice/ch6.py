'''
6-1 人 : 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中 的每项信息都打印出来。
'''
Cyril = {
	'first_name' : 'Cyril',
	'last_name' : 'Yen',
	'age' : 18,
	'city' : 'New Taipei'
}

print(Cyril)

'''
6-2 喜欢的数字 :使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键;想出每个人喜欢的一个数字，并将这些数字作为值存 储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
'''
infos = {
	'Cyril' : 22,
	'Joel' : 5566,
	'Mingy' : 87,
	'Mei' : 77,
	'Eric' : 88
}

print(infos)

'''
6-3 词汇表 :Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。 
'''

# 想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
methods = {
	'Max' : 'Get Max',
	'Min' : 'Get Min',
	'Len' : 'Get Length',
	'Sort' : 'Sort List',
	'type' : 'Get Variable Type'
}


# 以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义;也可在一行打印词汇，再使用换行符(\n )插 入一个空行，然后在下一行以缩进的方式打印词汇的含义。
print('Max : ' + methods['Max'])
print('Min : ' + methods['Min'])
print('Len : ' + methods['Len'])
print('Sort : ' + methods['Sort'])
print('type : ' + methods['type'])


'''
6-4 词汇表2 :既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。确定该 循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
'''
for key, value in methods.items():
	print(key + ' : ' + value)


'''
6-5河流:创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt'。 
'''
data = {
	'亚马逊河' : '巴西',
	'尼罗河' : '埃及',
	'长江' : '中国'
}

# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。 
for key, value in data.items():
	print(key + ' 穿越 ' + value)

# 使用循环将该字典中每条河流的名字都打印出来。
for name in data.keys():
	print(name)

# 使用循环将该字典包含的每个国家的名字都打印出来。
for country in data.values():
	print(country)


'''
6-6 调查 :在6.3.1节编写的程序favorite_languages.py中执行以下操作。 
'''
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。 
name_list = {
	'Cyril' : 'Done',
	'Joel' : 'New',
	'Mingy' : 'New',
	'Eric' : 'Done',
	'Mei' : 'Done'
}

# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
for key, value in name_list.items():
	if (value == 'Done'):
		print(key + ' 要準時到唷！')
	else:
		print(value + ' 快來參加唷！')

'''
6-7 人 :在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有 信息都打印出来。
'''
Mei = {
	'first_name' : 'Mei',
	'last_name' : 'Chen',
	'age' : 16,
	'city' : 'New Taipei'
}

Jack = {
	'first_name' : 'Jack',
	'last_name' : 'Ting',
	'age' : 28,
	'city' : 'New Taipei'
}

people = [Cyril, Mei, Jack]

for x in people:
	print(x)

'''
6-8 宠物 :创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名;在每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
'''
WonWon = {
	'type' : 'Dog',
	'master' : 'Cyril'
}

MiowMiow = {
	'type' : 'Cat',
	'master' : 'Mei'
}

pets = [WonWon, MiowMiow]

for x in pets:
	print(x)

'''
6-9 喜欢的地方 :创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键;对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练 习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
'''
favorite_places = {
	'Cyril' : ['Wulai', 'Xindan', 'Sonshan'],
	'Mei' : ['HK', 'US', 'lake'],
	'Ken' : ['Japan', 'China', 'Korea']
}

for key, value in favorite_places.items():
	print(key + ' : ' + str(value))

'''
6-10 喜欢的数字 :修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
'''
import random

for key in infos:
	temp = []
	for count in range(0, random.randint(1, 4)):
		temp.append(random.randint(0, 99))
	infos[key] = temp

for key, value in infos.items():
	print(key + ' : ' + str(value))

'''
6-11 城市 :创建一个名为cities 的字典，其中将三个城市名用作键;对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该
城市的事实。在表示每座城市的字典中，应包含country 、population 和fact 等键。将每座城市的名字以及有关它们的信息都打印出来。
'''
cities = {
	'Taipei' : {
		'country' : 'Taiwan',
		'population' : '1000w'
	},
	'Tokyo' : {
		'country' : 'Japan',
		'population' : '8000w'
	},
	'Beijin' : {
		'country' : 'China',
		'population' : '10000w'
	}
}

for city, info in cities.items():
	print(city + ' => ' + str(info))








