---
title: 《TypeIdeaBlog_1_1》  需求
date: 2018-03-15 01:54:56
categories: 《TypeIdeaBlog》笔记
tags:
	- Django
	- TypeIdeaBlog
---



## 写代码前，一定要弄清楚要写什么！

你写的代码是做什么用的？你最终要实现的是什么？你的需求是什么？

如果对需求没有明确的了解，整体的规划，最终结果可能做出来是并不是想要的。



## 一个项目的诞生： web/app

#### 需求的提出

来源：

- 企业用户
- 个人用户

由产品经理来收集和整理用户的需求，最终输出一份需求文档，叫PRD

#### 评审

整理好需求文档后，集合相关的人员 -- 开发，测试，运维，以及其他相关人员

这些人员一起对项目开发过程中可能涉及到的需求经过严格评审，最终形成十分明确和细化的需求

#### 系统设计

拿到明确的需求后从需求里面提炼出来功能点，做一个整体的设计，模块划分。

#### 技术选型

依据业务的特点，根据你的功能点，选择使用哪些合适的技术来实现。

#### 系统开发

进入实际的编码开发阶段



## 需求文档

#### 博客需求描述：

分为读者可访问部分和作者进行创作的部分

#### 读者访问需求如下：

- 需要能够通过搜索引擎搜索到博客内容，进而来到博客
- 可以在博客中进行关键词搜索，然后展示出文章列表
- 能够根据某个分类查看所有关于这一分类的文章
- 访问首页需要能看到有新到旧的文章列表，以便于查看最新的文章
- 需要能够通过RSS阅读器订阅博客的文章
- 要能够对某一篇文章进行评论
- 能够配置友链，方便与网友进行链接

#### 创作者的需求如下：

- 博客后台需要登录后方可进入
- 能够创建分类和标签
- 能够编写文章，以Markdown格式编写
- 能够配置导航，以便引导读者
- 作者更新后，读者能够收到通知







## 技术人员想两件事：

1. 这个需求合不合理 ？需求能不能支撑技术的实现？
2. 这个功能能不能做 ？如何去做？技术上可行性？


