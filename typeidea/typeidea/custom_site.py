#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
1. 检查先决条件
2. 定义子程序要解决的问题
3. 为子程序命名
4. 决定如何测试子程序
5. 在标准库中搜寻可用的功能
6. 考虑错误处理
7. 考虑效率问题
8. 研究算法和数据类型
9. 编写伪代码
    1. 首先简要地用一句话来写下该子程序的目的，
    2. 编写很高层次的伪代码
    3. 考虑数据
    4. 检查伪代码
10. 在伪代码中试验一些想法，留下最好的想法
'''

from django.contrib.admin import AdminSite


class Custom_Site(AdminSite):
    site_header = 'Typeidea 管理后台'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = Custom_Site(name='cus_admin')
