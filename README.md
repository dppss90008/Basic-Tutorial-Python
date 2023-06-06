# Python
Python is one of the most popular programing language.
###### tags: `python`

## 基礎篇章: 

###  Install python on you computer
1. Download the lastest version of [python](https://www.python.org/downloads/)
2. Difference between python2 and python3: some syntax are different
3. Integrated Development Environment (IDE): where you can write the python code. 
4. Few IDE are recommended: Anaconda (jupyter)、VS-code、PyCharm ...

### First python program
==Print function==
```python=3.8
# print function can show the string on the console

print("Hello world!")

# Python shows the instructions in order
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
```

### Variable 變數
可用來存放資料的自訂名稱。
在電腦的記憶體空間，用自訂的名稱進行宣告，可以用來放置任何資料。

```python=3.8
# name and age are variables 
# you can change the name and age here
name = "George"
age = 70

print("There once was a man named "+name+", ")
#str can change the int datatype to string 
print("he was "+str(age)+" years old, ") 
print("He really liked the name "+name+", ")
print("but didn't like being "+str(age))
```

等於在程式語言中的概念: 賦值運算子

### DataType 資料型態
* 數值型別 numeric type

| int | float | bool | complex |
| ------- | -------- | -------- |----|
| integer 整數     | 浮點數     | Boolean 布林數     | 虛數 |
| 不含小數 |含小數 | True、False、None | 1+5j|

```python=3.8
print(2.16) # float
print(3 * (4 + 5)) # () 可以提升運算優先度
print(10 % 3) # 取餘數...1
my_num = -5
print(abs(my_num)) # Get the absolute value of my_num
print(pow(4,6)) # Power function 
print(max(2,6)) # Get the max number
print(min(2,6)) # Get the min number
print(round(2.1415,2)) # Round the number

from math imort * # This the module
print(floor(3.7)) 
print(ceil(3.7))
print(sqrt(36)) # 開根號

True
False
```
* 字串型別 string type 
文字、字串使用單雙引號夾住 "string 1 'string'
雙引號內可以放置任意的文字
```python=3.8
# 字串可以相加
phrase = "Giraffe Academy"
print(phrase+" is cool!")
# Change the string into uppercase 
print(phrase.upper()) # Change to uppercase
print(phrase.lower()) # Change to lowercase
print(phrase.upper().isupper()) # Check if upper or not: True
print(len(phrase)) # Get the length of the string 
# Grab the first character 
print(phrase[0]) # Python start with 0: G
# Return the index
print(phrase.index("a")) # This function will return the index of a
# Output: 3
# Replace the string
print(phrase.replace("Giraffe","NewString"))
```
* 容器型別 container type 

| List | tuple | set | dict |
| ------- | -------- | -------- |----|
| 序對 | 串列     | 集合     | 字典 |
| V X |V V | X V | X V|

(順序、可更改內容)

* List 列表
什麼是列表? 肚子裡面可以裝其他的基本資料 (元素)
```python=3.8
語法: 中括號表示列表，裡面用逗號隔開不同的資料。
[3,4,5,6,7,"Hello"]
```

* Tuple 不可動列表
```python=3.8
語法: 小括號的列表，為不可以動的列表，裡面用逗號隔開不同的資料。
(3,4,5,6,7,"Hello")
```

* Set 集合
```python=3.8
語法: 大括號的列表，集合沒有順序的概念，沒有區分誰是第一、第二、第三。
{3,4,5,6,7}
```

* dict 字典
```python=3.8
語法: 大括號的列表。Key 跟數值的配對。
{"Key":Value,"Apple":"Red","Apple":"Red"}
```

### Python function 

```python=3.8
def say_hi(name): # name is the parameter
    print("Hello "+name)
    
say_hi("Jimmy") # call the function

def cube(num):
    return num*num*num # Return sth from the function

result = cube(3) 
# the variable result will store the value return from the function
```

### 條件判斷式
```python=3.8
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    
else:
    print("You are neither male nor tall")
```

* or: 任一對則對 True or False = True
* and: 兩者都得對 True and False = False 
* not: 將True變成False,False變成True. not(True) = False
* comparison operators == >= <= < >


### 迴圈
```python=3.8
fruits = ["Apple","Water melon","strawberry"]

for fruit in fruits:
    print(fruit)
    
for i in range(len(furits)):
    print(fruits[i])
    
for i, fruit in enumerate (fruits):
    print(i)
    print(fruit)d
```

### 無窮迴圈
```python=3.8
i = 0 
while True:
    print(i)
    i += 1 
```
終止無窮迴圈的方法

```python=3.8
i = 0 
while i < 10:
    print(i)
    i += 1 
```


### Read/write the file
```python=3.8
with open("file.txt","r") as file:
    text = file.readlines()

with open("file.txt","w") as file:
    file.write("some message")
    
with open("file.txt","a") as file:
    file.write("append some message")

# Another method read or write the file
file = open("file.txt","r")
text = file.readlines()
file.close()
```

### Module 模組
```python=3.8
# useful_tools.py
def some_function():
    return sth
    
# app.py
import useful_tools
# Then, you can use the function from the useful_tools.py
useful_tools.some_function()

import useful_tools as ut
ut.some_function()

from useful_tools import some_function
some_function()
```

## 進階篇章:

### 網頁爬蟲

### 

### 多執行緒運算 (平行處理)
==mutiprocessing==
```python=3.8
import itertools
import multiprocessing

def RunParallel(par):
    
    # 每一次平行化，接收到一個(tuple)
    parmeterA = par[1] #將參數拆解出來
    parmeterB = par[0]

    try:
        with open("xxx.csv","a") as file:
            # 兩個參數傳入自定的functionA之中
            # 並使用寫檔輸出("a"模式)
            val = functionA(A=parmeterA,B=parmeterB) 
            file.write(val+"\n")
    except:
        pass

if __name__ == '__main__':
    # 設定多行程核心數
    pool = multiprocessing.Pool(60)
    # 傳入資料 indexs 於RunParallel function
    # indexs = [(1,a),(2,b),(3,c),....]
    # 每一個(tuple)平行化傳入
    res = pool.map(RunParallel,indexs) 
    pool.close()

```


### 子行程操作處理
==mutiprocessing==
```python=3.8
from subprocess import Popen,PIPE,call

# 使用 list傳入(如果有多個參數需要設定時)
command = [program,"--參數1",參數1數值,"--outdir",outdir]
run_code = Popen(command,shell=False,stdout=PIPE,stderr=PIPE,encoding="ascii")
stdout, stderr = run_code.communicate() #運行，如果是標準化輸出，stdout可以接收結果
   
# 直接呼叫
call("shell script",shell=True) # 語法
call("echo Hello world",shell=True) # 範例
```