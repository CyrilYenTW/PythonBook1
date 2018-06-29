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
結果
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
結果
```
 PythonLanguage
Python Language
PythonLanguage
```  





