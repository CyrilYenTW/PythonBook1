
# 2-1 将一条消息存储到变量中，再将其打印出来。
message = "Hello World"

print(message)


# 2-2 将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。
message = "Message One"

print(message)

message = "Hello Python"

print(message)


# 2-3 个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息。
name = 'Cyril'
print('Hi ' + name + '!!')


# 2-4 调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name = 'cyril'

print(name.upper())
print(name.lower())
print(name.title())


# 2-5 名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
print('Albert Einstein oncesaid,“Apersonwho never madea mistake never tried anything new.”')


# 2-6 名言2： 重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
famous_person = 'Albert Einstein oncesaid'
message = '“Apersonwho never madea mistake never tried anything new.”'

print(famous_person + ',' + message)


# 2-7 
#	1.剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
#	2.打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
name = '\tCyril\t'

print(name.lstrip()+'\n'+name.rstrip()+'\n'+name.strip())


# 2-8 编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。为使用print 语句来显示结果，务必将这些表达式用括号括起来
print(3+5)
print(10-2)
print(2*4)
print(16/2)


# 2-9 最喜欢的数字： 将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。
number = 1022
print('My Favorate Number is ' + str(number))


# 2-11 Python之禅： 在Python终端会话中执行命令import this ，并粗略地浏览一下其他的指导原则
import this