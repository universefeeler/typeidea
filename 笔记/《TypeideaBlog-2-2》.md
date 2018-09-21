---
title: 《TypeideaBlog_2_2》 Python框架基础 -- WSGI的原理和实现
date: 2018-04-01 11:45:15
categories: 《TypeIdeaBlog》笔记
tags:
	- Django
	- TypeIdeaBlog
---


大部分Python框架是基于WSGI协议实现，也有部分是基于socket实现

![mage-20180401114847](/var/folders/y0/dvj7d_jd53sgldw8lpfk0d3m0000gn/T/abnerworks.Typora/image-201804011148473.png)

本节内容与过往总结重复，参见 [从输入URL到页面加载完成发生了什么-WSGI协议与实现](https://huangke19.github.io/2018/03/05/%E4%BB%8E%E8%BE%93%E5%85%A5URL%E5%88%B0%E9%A1%B5%E9%9D%A2%E5%8A%A0%E8%BD%BD%E5%AE%8C%E6%88%90%E5%8F%91%E7%94%9F%E4%BA%86%E4%BB%80%E4%B9%88-WSGI%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%AE%9E%E7%8E%B0/)



## 一个简单的请求流程

1. 用户请求一个域名，进行域名解析
2. 通过域名解析后，请求连到 Nginx上，把HTTP协议发给Nginx
3. Nginx拿到HTTP数据后，把数据转发到upstream上，
4. 通过协议（socket,WSGI）或端口的方式转发到容器(gunicorn，uwsgi)上
5. 容器也叫web server，web server之后就是application/framework，application需要放到容器上来跑
6. application/framework需要实现一个callable方法。
7. 应用或框架会把HTTP请求封装成一个Request对象，是为了用起来更方便
8. 拿到Request对象后就可以进行相应的操作，然后将处理结果封装成Response，返回给容器

WSGI协议其实也是通过socket绑定到某个端口上，来对外提供服务，其他非使用WSGI的直接使用socket。

