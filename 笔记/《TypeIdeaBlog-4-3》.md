---
title: 《TypeIdeaBlog_4_3》 合理的项目结构
date: 2018-04-14 20:10:54
categories: 《TypeIdeaBlog》笔记
tags:
	- Django
	- TypeIdeaBlog
---



## 规划

如何去规划你的项目结构？才能保证团队开发时候的高效率  

> -  不同的人维护不同的文件  
> - 不同的业务、需求去修改不同的文件代码

而不是所有的东西混乱，夹杂在一块儿



## 项目结构

> ```shell
> project 
>
> 	# 通过典型的python来打包
> 	setup.py    
> 	
> 	# 配置文件存放的文件夹
> 	conf		
> 		nginx.conf
> 		supervisored.conf
>         
>     # fabric文件夹
>     fabfile		
>     
>     # 项目需要的库和版本
>     requirements.txt	
>     
>     # git忽略的文件 
>     .gitignore	
>     
>     # settings文件夹，用以区分线上环境和线下环境
>     settings	
> ```



## 拆分配置文件 

区分线上线下，开发、测试、线上环境

> 1. 将settings.py文件改成一个模块/文件夹
>
> 2. 将settings.py移入settings文件夹
>
> 3. 删除settings.pyc文件，不然导入会从此文件导入 
>
> 4. 将settings.py改为base.py作为基础文件
>
> 5. touch develop.py
>
>    ```python
>    # noqa的意思是免除对导入*的检查，pep8不建议直接导入*所有
>    from .base import *  #noqa    
>
>    # 覆盖base里的设置
>    DEBUG = True
>    ALLOWED_HOSTS = [*]
>
>    DATABASES = {
>        'default': {
>            'ENGINE': 'django.db.backends.sqlite3',
>            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
>        }
>    }
>    ```
>
> 6. touch product.py
>
>    ```python
>    # 同上，但是某些选项针对生产环境进行修改
>    ```
>
> 7. touch test.py
>
>    ```python
>    # 同上，略
>    ```
>
> 8. 直接启动会出现找不到settings.py的错误，对此在manage.py中修改即可
>
>    ```python
>    # 通过环境变量决定启用的配置文件 
>
>    profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
>    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)
>    ```
>
>    ```shell
>    # 启用生产环境配置
>    export TYPEIDEA_PROFILE=product
>    ```



#### 对于不同的环境，还可以配置加载不同的模块

```python
INSTALLED_APPS += [
    'api',
]
```



## 总结

通过拆分配置文件，使得项目在生产环境、测试环境、开发环境分别使用不同的配置，加载不同的模块来提供服务