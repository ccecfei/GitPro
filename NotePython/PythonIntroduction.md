### 运算
/    表示浮点除

//   表示整除

%求余数

* divmod(a, b)返回(整除结果，余数)
	* divmod(9, 5) -> (1,4)

### 类型转换

* int() 
* float()
* str()

### string

* 三种形式

```python
x = 'abc'
y = "aaaa'b'cccc"
z = '''abc
	defg
	'''
```

* `s.join(str_list)`

用s把str_list里的每个成员连接起来，最后组成一个字符串

 


### 切片 slice[start, end, step]

```python
s = 'uvwxyz'
s[2:4]    -> 'wx'   #从头切
s[-5:-2]  -> 'vwx'  #从尾切

```

## sequence 序列

* string
* list
* tuple

### 常用操作

* create

```	python
	la = [] #方括号方法纯粹用来新建一个新的list
	lb = list('cat') -> ['c', 'a', 't'] #list()方法还可以以其它seqence作为参数，将其转换为一个list
```	

* 用下标可以获取指定的item

* 插入item用`L.insert(idx, item)`

* 末尾添加item
	* 最后面添加item，用`L.append()`
	* 最后面添加list，用`L.extend()`

> NOTE:如果用append()在最后加入一个list,那么这个list会作为一个item加入到末尾

* 利用下标删除item 用del语句 `del L[idx]`

	注意：
	
	1. del之所以不是成员函数，是因为python的gc需要这个释放信息，以便进行回收。
	2. del所做的工作：断开这个变量名与对象之间的关系，如果这个变量名是此变量的最后一个引用，那么就释放此对象的内存
	3. del是一个python语句，而不是函数。他的操作对任何python对明有效，而不仅仅限于list

* 删除指定value的item,而不关系心此item的具体位置。用`L.remove(v)`
* `L.pop(idx)`：删除与返回指定idx位置的值
* `L.index(value)` 返回此value第一次出现的下标
* `L.count(value)` 返回此value的个数
* `value in L` in语句，测试value是否在L里面

### sort

* `L.sort()` 成员函数，就地排序
* `sorted()` 通用函数，返回一个有序copy

### copy的三种方法，都是返回一个全新的list
* `L.copy()`
* `list(l_src)` 
* `L[:]` 切片



两个排序函数都可以加上`reverse=False`来进行倒序排序

### tuple

create

```python
 	ta = ('a',) # 对于只有一个元素的tuple,后面一定要加逗号!
 	tb = tuple('cat')
```

注意tuple的特殊之处：

```python
	ta = 'a',
	a, b = 'hello', 'world'
	a, b = b, a #等价于 a, b  = (b, a)
```

只要结尾带了逗号，就被认为是一个tuple，如第1行

因此，第三行的交换变量，实际上是右边的b,a被看成一个tuple，当被赋值的时候，如果左边有多个变量，这个时候tuple会自动拆箱

### dict 

* create

```python
	da = {}
	
	db = dict( [['a', 'x'], ['b', 'y'], ['c', 'z']] )
	dc = dict( ['ax', 'by', 'cz'] )
```

注意第二种形式，可以看出dict()对参数要求两点：

1. 外层是序列
2. 内层是长度为2的序列

* `D.update(otherDict)`连接两个dict
	* 连接时如果key冲突，则以第二个为准

* `D.clear()` 清空整个dict
* `D.get(key, 'default value')` 若key不存在，则返回默认值
* `D.keys()` 返回所有的key,类型为dict_keys，可迭代（这是python3，在2里，返回list类型）
* `D.values()` 返回所有value
* `D.items()` 返回所有的K-V对

### set

* create

```python
	sa = {'a', 'b'}
	sb = set('abc')
	sc = set( {'a':1, 'b':2} ) # ('a', 'b')
```

* 注意：
	* 不能使用｛｝来创建一个空的set，因为这个花括号被dict占用了
	* 若set()的参数是一个dict,则只使用key来转化。换句话说，鬼知道value里存的什么鬼，完全有可能是不能转化的东西

* 集合操作

```python
	# 交集
	sa & sb
	sa.intersection(sb)
	
	# 并集
	sa | sb
	sa.union(sb)
	
	# 差集
	sa - sb
	sa.difference(sb)
	
	# 交集取反
	sa ^ sb
	sa.symmetric_diffrence(sb)
	
	# 是否是子集
	sa <= sb
	sa.issubset(sb)
```


 	


### join() 
* list转化为string:`‘,’.join(L)`
* join()可以作用在所有的可迭代对象上，因此把它设计成string而不是list的成员函数，可以方便的把其它所有可迭代类型转化为string


### python statement / python的一些通用语句或函数
* len()

* del

```python
	del L[idx]
	del D[key]
```

* in

```python3
	value in L
	key in D
	value in S
```

### 哪些是False

1. 0
1. None
2. False
3. 空序列

* 注意None和False的区别：

```python
	### None & False都不符合
	if something: 
		print 'aaa'
	else:
		print 'bbb'
		
	### 只有None才会进if分支
	if something is None:
		print 'aaa'
	else:
		print 'bbb'

```

### 循环的break用else来检测

### 迭代

* dict的三种迭代：

```python
	D.keys()
	D.values()
	D.items() # 每个item都是(k,v)的tuple

```

* `zip(sequenceA, sequenceB)` 
	* 一次迭代多个容器
	* 最短的容器遍历完时就停止
	* 实际上，zip()是把各容器的同下标元素组成一个tuple, 然后这些tuple再组成一个list

### 推导

* 意义：将‘循环’ 与 ‘条件过滤’以紧凑的形式表达


```python
	# list推导
	[exp for item in iterable] 
	[exp for item in iterable if condition]
	[ n^2 for n in range(5) ]
	
	# dict推导
	{ key_exp: value_exp for exp in iterable }
	word = 'Hello World'
	letterCount = { letter: word.count() for letter in word } # word字符串里每个字母出现的次数
	
	# set推导
	{ n^2 for n in range(5) } # 和list一样，变成花括号包起来
	
	
	[ n for n in range(5) if n%2 == 1 ]
	# 上面的推导可以展开为：	
	l = []
	for n in range(5):
		if n%2 == 1:
			l.append(n)

```

* 生成器推导

	1. 生成器是特殊的，用yield抛出一个值，而不是return
		* 生成是“序列创建”对象，可以被迭代
		* 每次被迭代的时候，生成器都会保存上次被调用的位置，然后返回下一个值 
	2. 生成器只能被迭代一次，再次迭代返回空
	3. list()可直接把生成器转化为list

```python
	( n for n in range(5) if n%2 == 1 ) # 和list一样，只不过变成小括号

``` 

上面的生成器可以展开为：

```python
	def myRange():
		for n in range(5):
			if n%2 == 1:
				yield n # 不是return!
	
	myRange # myRange是一个函数
	called = myRange()
	called # called是由myRange()返回，是一个生成器，可以被迭代

```

### 函数

函数要点：函数是一等公民，是一个对象

1. 可赋给其它变量
2. 可作为参数传递 
3. 可作为函数的返回值 

参数默认值

1. 默认值只会在函数定义的时候执行一次，而不是在run的时候
2. 不会随函数的结束而消失，可理解为全局变量，只不过作用域是整个函数

可变参数

1. 格式 `def func(*args)`
2. 实质 *号把位置序参数转化为tuple, 当作一个整体

关键字参数

1. 格式 `def func(**kwargs)`
2. 实质 `**`把关键字参数组成一个dict

Docstrings

* doc放在函数体的最开头，用字符串表示，用help(funcName)来访问

### 闭包

1. 内部函数的概念

2. 如果外部函数直接返回了内部函灵本身（inner），而不是内部函数的调用（inner()），那么就形成了一个闭包
3. 内部函数可以直接访问外部函数的变量
4. 每次调用外部函数都会动态的返回一个函数（也就是闭包）
5. 下次调用这个闭包的时候，他会记住自己的外部变量

```python
	def outer(word):
		def inner():
			print 'inner can access outer`s varies ', word
		return inner
	
	a = outer('Hello') # 返回一个闭包
	
	type(a) # a的类型 <class 'function'>
	a       # a是什么 <function outer.<locals>.inner at 0xFFFFF..>
	a()     # 调用这个闭包 inner can access outer's varies Hello

```

### 装饰器的本质

```python
	def before(func):
		def wrapper(a, b):
			print 'Run func:', func.__name__
			func(a, b)
		return wrapper # 记住最后要返回这个函数
	
	def plus(a, b):
		return a+b
		
	# 使用
	newPlus = before(plus)
	newPlus(1, 2)
	
	# 语法糖
	@before
	def plus(a, b):
		pass
	# 上面的实质是做了：plus = before(plus)
	

```

### 全局变量

全局变量要先global声明，再使用，不能合为一行

```python
	global a
	a = 'dog'

```

下面两个函数返回对应命名空间的内容，都是dict:
	1. locals()
	2. globals()

### try catch except

```python
	try:
		doSth()
	except: # 不带参数，捕获任意异常
		doHandle()

	# 带参数，捕获对应异常
	except exceptionType:
	
	# 带as,可以获得这个异常对象
	except exceptionType as name
	
	# 比如
	try:
		raise OopsException('memory leaked!')
	except Exception as e:
		print(e) # memory leaked! 会把抛出异常时所带的消息打出来

```

编写自己的异常

1. 自己的异常都必须是Exception的子类


## 模块

命令行参数，用`sys.argv`来获取

`sys.path` 表示模块搜索路径，其第一个值为空字符，指程序运行的当前目录

### 导入模块

模块名，就是python文件名

模块导入的四种方式如下：

```python
import module
import module as m
from module import something
from module import something as sth

```























