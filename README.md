# Python 編程: 從入門到實踐
學習 Python 的第一本書, 用此書的原因是因為他每個小章節後面都有一些練習的題目可以做做看  

## 第一章 起步
* 開發環境  
因為有兩台電腦, 沒有一直在同一個環境下學習 Python  
所以開發環境為 Windows 10、 OSX  

* 使用軟體  
Sublime Text 3  
Git  

## 第二章 变量和简单数据类型

### 2-2 变量
* 不需要宣告直接命名變數接值即可
```
mesaage = 'hello world'
```
  
### 2-3 字符串
* 修改字串大小寫
```
message = 'hello world'
print(message.title()) # Hello World
print(message.upper()) # HELLO WORLD
print(message.lower()) # hello world
```

* 使用 單引號('') 或 雙引號("") 將字串包起來  
```
print('hello world') # hello world
print("hello world") # hello world
```

* 合併字串使用加號(+)
```
 print('I' + ' Love' + ' Python') # I Love Python
```  

* 換行符號(\n), 添加空白(\t)
```
print('\tPython\nLanguage')
```
```
	Python
Language
```  

* 刪除空白, 刪除右空白 rstrip(), 刪除左空白 lstrip(), 刪除左右空白 strip()
```
message = ' Python '
print(message.rstrip()+'Language')
print(message.lstrip()+'Language')
print(message.strip()+'Language')
```  
```
 PythonLanguage
Python Language
PythonLanguage
```

### 2-4 數字

* 整數四則運算, 加(+)、 減(-)、 乘(＊)、 除(/)  
```
print(4+2) # 6
print(4-2) # 2
print(4*2) # 8
print(4/2) # 2
```

* 乘方 (＊＊)　　
```
print(3**3) # 27
```

* 浮點數, 直接宣告即可
```
number = 0.3
print(number) # 0.3
print(number+2) # 2.3
print(number*2) # 0.6
```

* 使用 str()
```
age = '30'
print('Happy' + str(str) + 'rd Birthday')
# Happy 30rd Birthday
```

### 2-5 註釋
* 單行註釋使用井字符號(#)
```
#這是一行註釋
```

### 2-6 Python 之禪
```
import this
```
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 第三章 列表簡介

### 3-1 列表是甚麼

* 列表使用中括號([])表示
```
colors = ['red', 'blue', 'white', 'black']
print(colors)
```
```
['red', 'blue', 'white', 'black']
```

* 訪問列表元素, 使用 " 變數名稱[索引編號] ", ※索引邊號從 0 開始
```
colors = ['red', 'blue', 'white', 'black']
print(colors[0]) # red
```

### 3-2 修改、添加和刪除元素
* 修改, 直接呼叫賦值 "變數[索引編號]=新值 "
```
colors = ['red', 'blue']
colors[1] = 'white'
print(colors) # ['red', 'white']
```

* 列表中添加元素, 使用 append('新值')
```
colors = ['red', 'blue']
colors.append('black')
print(colors) # ['red', 'blue', 'black']
```

* 列表中插入元素, 使用 insert(索引, '新值')
```
words = ['A','B','C']
words.insert(1, 'D')
print(words) # ['A', 'D', 'B', 'C']
```

* 從列表中刪除元素, 使用 del 列表名稱[索引]
```
words = ['A','B','C']
del words[1]
print(words) # ['A', 'C']
```

* 使用 pop() 刪除元素, pop() 是將最後一筆元素刪除並回傳刪除的元素, 故可以使用變量承接
```
words = ['A', 'D', 'E']
item = words.pop()
print(words)
print(item)
```
```
['A', 'D']
E
```

* 使用 pop(索引) 刪除元素, pop() 可以指定要移除的元素並回傳該元素
```
words = ['A', 'D', 'E']
item = words.pop(1)
print(words)
print(item)
```
```
['A', 'E']
D
```

* 根據值刪除元素, 使用 remove('值')
```
colors = ['red', 'black', 'white']
colors.remove('black')
print(colors)
```
```
['red', 'white']
```

### 3-3 組織列表

* 使用方法 sort() 進行永久排續
```
cars = ['BMW', 'Toyota', 'Benz', 'Subaru', 'Audi']
cars.sort()
print(cars)
```
```
['Audi', 'BMW', 'Benz', 'Subaru', 'Toyota']
```

* 使用方法 sorted() 進行臨時排序
```
cars = ['BMW', 'Toyota', 'Benz', 'Subaru', 'Audi']
print(sorted(cars))
print(cars)
```
['Audi', 'BMW', 'Benz', 'Subaru', 'Toyota']
['BMW', 'Toyota', 'Benz', 'Subaru', 'Audi']
```
```

* 使用方法 reverse() 進行列表反轉
```
cars = ['BMW', 'Toyota', 'Benz', 'Subaru', 'Audi']
cars.reverse()
print(cars)
```
```
cars = ['BMW', 'Toyota', 'Benz', 'Subaru', 'Audi']
```

* 使用方法 len(列表名稱) 取得列表長度
```
cars = ['BMW', 'Toyota', 'Benz', 'Subaru', 'Audi']
print(len(cars)) # 5
```

* 使用列表的注意事項  
　　　使用索引必須在有效的長度內  
　　　索引從 0 開始計算  


## 第四章 操作列表

### 4-1 遍历整个列表

* 使用 for 迴圈循環打定
```
countries = ['Taiwan', 'Japan', 'Korea']

for country in countries:
	print(country)

```
```
Taiwan
Japan
Korea
```

* 在 for 循環中執行更多的操作
```
countries = ['Taiwan', 'Japan', 'Korea']
prefix = 'I want to go to '
for country in countries:
	print(prefix + country + '!!')
```
```
I want to go to Taiwan!!
I want to go to Japan!!
I want to go to Korea!!
```

* 在for 循环结束后执行一些操作, "缩进是重點"
```
countries = ['Taiwan', 'Japan', 'Korea']
prefix = 'I want to go to '
for country in countries:
	print(prefix + country + '!!')

print("I'm no money!!")
```
```
I want to go to Taiwan!!
I want to go to Japan!!
I want to go to Korea!!
I'm no money!!
```

## 4-2 常見的缩进错误

* 忘記缩进
```
for country in countries:
print(country)
```

* 不必要的缩进
```
print('A')
	print(B)
```

* 循還後不必要的缩进
```
for country in countries:
	print(country)

	print('Done') # 空一行並不代表 for 迴圈的結束
```

* 遺漏冒號
```
for country in countries # 少了冒號
print(country)
```

