---
title: 《TypeIdeaBlog-2-4》 Tornado框架
date: 2018-04-12 17:25:46
categories: 《TypeIdeaBlog》笔记
tags:
	- Django
	- TypeIdeaBlog
---



## Tornado优点

相对于Flask来说，Tornado最明显的特点是高性能，它的特性是异步非阻塞，它只是做了一个基本的HTTP协议的封装，封装一个Request和一个Response过来，需要自己来实现其他的部分，比如说session.

Tornado的卖点就是性能，可以直接通过socket的方式来实现一个Webserver，Tornado就是基于此来做的，它并没有直接用WSGI协议，因为WSGI是一个同步的协议，它只暴露了方法给你，



## Tornado内置的功能

- tornado.web — RequestHandler and Application classes （基础的Request的封装）
- tornado.template — Flexible output generation（简单的模板系统）
- tornado.routing — Basic routing implementation（基础的路由配置）
- tornado.escape — Escaping and string manipulation （转码和字符串的操作）
- tornado.locale — Internationalization support （国际化的支持）
- tornado.websocket — Bidirectional communication to the browser（Websocket的支持）



通过非阻塞的网络I/O，Tornado能够支撑成千上万的连接，这使它很适合对每个用户都需要建立长连接的需求，无论是通过long polling(长轮询) Websockets，或者其他应用，Tornado适合的场景是长连接。

#### 长连接：

 在使用长连接的情况下，当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，客户端再次访问这个服务器时，会继续使用这一条已经建立的连接。Keep-Alive不会永久保持连接，它有一个保持时间，可以在不同的服务器软件（如Apache）中设定这个时间。实现长连接需要客户端和服务端都支持长连接。



Torando并不只是一个Web框架，它还可以用来做高性能爬虫，压测工具等



## 总结

在Python2.x环境中，基于event loop模型的Tornado很有优势，但在Python3.x中，语言内部支持了event loop，这样更多的框架可以很容易的开发出异步非阻塞模型，不过综合来说，Tornado依然是当前实践经验最丰富的异步非阻塞框架。



