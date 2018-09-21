---
title: 《TypeIdeaBlog_4_1》编码规范 1
date: 2018-04-12 20:45:51
categories: 《TypeIdeaBlog》笔记
tags:
	- Django
	- TypeIdeaBlog
---

## 规范

项目开始前应该统一一下大家的一些共识，比如我们编码规范，虚拟环境，项目结构，git协作方式，有了这些基础后，再来做项目的搭建，这样协作起来会更加的高效。



## 编码规范

对于新手的个人项目，代码没有规范也不是大问题，但是对于团队来说，编写的代码应该有一致的风格，否则整个代码看起来会十分凌乱，不同成员不同的编码方式、习惯，让阅读者很难适应。



关于编码规范，如果你所在团队有自己的规范的话，可以不用完全遵循Python的编码规范，但是即使如此，也应该去了解下PEP8，Python官方建议的编码规范，因为大部分团队遵循的是官方的规范，你应该有意识的去对比你所在团队的编码规范跟官方规范有何不同，优缺点是什么？



## 官方规范 — Python之禅

```python
import this
```

> The Zen of Python, by Tim Peters
>
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!



## [Google Python编码规范](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/)



#### 分号

> ​	不要在行尾加分号, 也不要用分号将两条命令放在同一行.



#### 行长度

> ​	每行不超过80个字符
>
> ​	不要使用反斜杠连接行，如果代码过长，可以使用圆括号, 中括号和花括号隐式的把行连接起来



#### 括号

> ​	宁缺毋滥的使用括号



#### 缩进

> ​	用4个空格来缩进代码，把tab键设置为4个空格

更多请参考链接 http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/



#### 空格

> 顶级定义之间空两行, 比如函数或者类定义. 
>
> 方法定义, 类定义与第一个方法之间, 都应该空一行.
>
> 对于自定义的代码块，不同的逻辑之间可以用空行来区分



#### 引入顺序

> 内置库
>
> 第三方库
>
> 自己



#### 空格

> 等号两边需要空格
>
> 括号内不要有空格.
>
> 不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾).
>
> 参数列表, 索引或切片的左括号前不应加空格.



#### Shebang

> 大部分.py文件不必以#!作为文件的开始. 根据 [PEP-394](http://www.python.org/dev/peps/pep-0394/) , 程序的main文件应该以 #!/usr/bin/python2或者 #!/usr/bin/python3开始.



#### 注释

> 解释你的业务，而不是解释你的代码 



#### 类

> 如果一个类不继承自其它类, 就显式的从object继承. 嵌套类也一样.
>
> Django2.0会完全的抛弃掉Python2的语法，所以它不会显示的继承object，它默认就是新式类
>
> 对于Python3，也是默认为新式类



#### MRO继承顺序

```python
# 示例

# coding:utf-8
import inspect 

# 旧式类
class Base:
    def say(self):
        print('Base.say')
   
# 新式类
class Base(object:
    def say(self):
        print('Base.say')
        
class A(Base):
    pass


class B(Base):
    def say(self):
        print('B.say')
        
        
class C(A, B):
    pass


c = C()
c.say()
print(inspect.getmro(C))
print(dir(c))


对于旧式类：它是深度优先，先在A中找，找不到在Base中找，再找不到在B中找
对于新式类：它是菱形继承，先在左边往上寻找，再在右边往上寻找，最后在Base类里寻找 
```



#### 字符串

> 避免在循环中用+和+=操作符来累加字符串. 由于字符串是不可变的, 这样做会创建不必要的临时对象, 并且导致二次方而不是线性的运行时间. 作为替代方案, 你可以将每个子串加入列表, 然后在循环结束后用 `.join` 连接列表. (也可以将每个子串写入一个 `cStringIO.StringIO` 缓存中.)

字符串的高效使用：

> 字符串是不可变对象，每次对对象做操作都会生成一份新的对象，这就意味着如果你是在一个循环里操作，	就会占用很大的内存，如果需要拼接大量字符串，推荐使用列表的append操作和join综合进行拼接



#### 文件 

> 上下的管理 — 打开和关闭的动作要统一：如果有打开，就一定要有关闭

在Python中提供了with语句，创建一个上下文环境，它可以帮你自动的关闭

```python
with open("hello.txt") as hello_file:
    for line in hello_file:
        print line
```



#### TODO注释

> TODO注释应该在所有开头处包含“TODO”字符串，紧跟着是用括号括起来的你的名字，email地址或其他符号，然后是一个可选的冒号，接着必须有一行注释，解释要做什么

```python
def foo(arg):
    """ xxx """
    # TODO: 处理xx接口，等xx同学完成后进行开发
```



#### 导入格式 

> 每个导入应该单独占一行

```python
# yes
import os
import sys

# no
import os, sys
```

> 导入总是应该放在文件顶部，位于模块注释和文档字符串之后，模块全局癌变和常量之前
>
> 导入顺序：
>
> - 标准库导入
> - 第三方库导入
> - 应用程序导入



#### 语句

> 每条语句应该单独占一行



#### 访问控制

> 单下划线 — 表示私有变量，外部的调用尽量不要去调用私有变量，直接调用出错不负责
>
> 双下划线 — dunder变量
>
> 使用@property对内变量设置为属性

```python
class Foo(object):
    _name = 'huangke'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, value):
        self._name = value
```



To be continued …



```python
# TODO: to be continued after 24 min
```

