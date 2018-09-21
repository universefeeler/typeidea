---
title: 《TypeIdeaBlog_3_1》 如何阅读Django文档 
date: 2018-03-15 11:26:47
categories: 《TypeIdeaBlog》笔记
tags:
	- Django
	- TypeIdeaBlog
---



## Django结构

Django是基于MVC模式的框架，也被称为MTV模式，无论是MVC，MTV或是其他什么模式，目的都是解耦，把一个软件系统划分为一层一层的结构，就像计算机网络划分为七层一样，让每一层的逻辑更纯粹，便于开发人员维护，这其实就是一次大的抽象，这又回到了计算机软件的原则 — 抽象。



![](http://django-practice-book.com/images/django-layers.png)



#### 数据进入：

一个数据经过WSGI，传到我们的框架里面，会经过Middleware，Miidleware其实只是对你处理特定需求的handler的封装，Middleware会去调你的View，View去调DB

#### 数据返回：

DB — Model — View — View中把数据填充到Form里面 — Template里面渲染Form — 最后生成一个Response — Response通过Middleware再返回



一个成熟的框架，能让你把关注点放在特定的层面，而不需要去过分关心和其他部分的联系，比如View层，关注于处理逻辑，而不是直接去操作数据库。



## 文档结构

从大的划分来说，Django文档的核心模块

- The model layer
- The view layer
- The template layer
- Forms 

剩下的部分都是功能文档，比如Paginations, Caching, Loging等。



#### The model layer

ORM帮我们做两件事

1. 第一是从对象实体到数据库里的表进行映射

2. 第二是从数据到对象的映射       

   ```python
   User.object.all()  # select * from User;
   ```

   ​

