# 3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names = ['cyril', 'alex', 'adam', 'kyle']
print(names)

# 3-2 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
print('Hi ' + names[0] + '!!')
print('Hi ' + names[1] + '!!')
print('Hi ' + names[2] + '!!')
print('Hi ' + names[3] + '!!')

# 3-3 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，
transportation = ['Car', 'Bicycle', 'Motocycle']
print('I would like to own a ' + transportation[0]);
print('I would like to own a ' + transportation[1]);
print('I would like to own a ' + transportation[2]);

'''	
3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用
	这个列表打印消息，邀请这些人来与你共进晚餐。
'''
names = ['Cyril', 'Alex', 'Kle']
message = ' May I have a dinner with you?'

print('Hi ' + names[0] + message)
print('Hi ' + names[1] + message)
print('Hi ' + names[2] + message)


'''
3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
	以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
	修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
	再次打印一系列消息，向名单中的每位嘉宾发出邀请。
'''
# 要移除的名子
del_name = names.pop(1)
print(del_name + ' will be remove!!')

# 要新增的名子
new_name = 'Adam'
names.insert(1, new_name)
print(names)


'''
3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
	以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
	使用insert() 将一位新嘉宾添加到名单开头。
	使用insert() 将另一位新嘉宾添加到名单中间。
	使用append() 将最后一位新嘉宾添加到名单末尾。
	打印一系列消息，向名单中的每位嘉宾发出邀请。
'''
print('names => ' + str(names))

# 新增一位名子到開頭
names.insert(0, 'Alex')
print('names => ' + str(names))

# 新增一位名子在中間
names.insert(round(len(names)/2), 'EJ')
print('names => ' + str(names))

# 添加一位名子在最後
names.append('Scott')
print('names =>' + str(names))


'''
3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
	以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
	使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
	晚餐。
	对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
	使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
'''
name = names.pop()
print(name + '. Sorry you can\'t eat!!')

name = names.pop()
print(name + '. Sorry you can\'t eat!!')

name = names.pop()
print(name + '. Sorry you can\'t eat!!')

name = names.pop()
print(name + '. Sorry you can\'t eat!!')

name = names[0]
print(name + '. You can eat!!')

name = names[1]
print(name + '. You can eat!!')

del names[1]
del names[0]


'''
3-8 放眼世界 ：想出至少5个你渴望去旅游的地方。
'''
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
countries = ['Taiwan', 'Japan', 'Korea', 'Italy', 'China']

# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
print(countries)

# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。
print(sorted(countries))

# 再次打印该列表，核实排列顺序未变。
print(countries)

# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
temp = sorted(countries)
temp.reverse()
print(temp)

# 再次打印该列表，核实排列顺序未变。
print(countries)

# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
countries.reverse()
print(countries)

# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
countries.reverse()
print(countries)

# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
countries.sort()
print(countries)

# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
countries.reverse()
print(countries)


'''
3-9 晚餐嘉宾 ：在完成练习3-4~练习3-7时编写的程序之一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
'''
print('Country Count => ' + str(len(countries)));
