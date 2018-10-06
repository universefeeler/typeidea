# Model层，项目的基石



通过commit，我们每次提交的内容都是记录在案的。

在一个完整的项目中，可能有不同的app，每个app是你抽象出来的一部分业务，这部分业务可能关联性比较强，就把它放在一个app里面，如果关联性不强，就放在不同的app中。

TypeIdea的app划分是通过模型来进行划分的。

对于内容管理系统来说，时间是一个非常重要的概念。



## 创建模型

对一个模型的CharField，在Python里中文默认使用unicode，而在MySQL中是用的utf-8，

- max_length对应的是数据库中的varchar()
- blank默认为False，如果为True则可以为空
- verbose_name是后台显示名称

- ForeignKey()

  如果外键关联的模型还没建立时，外键字段就会报错

  对于Post这个类来说，category是它的一个成员属性，或者称为类级属性，类级属性的特点就是我在这个类被创建的时候，成员属性就会被创建。也就是说，在你import的时候，它就会执行这个属性

  ```python
  def say_hi():
      print("hi")
      return 'hi'
  
  
  class Foo(object):
      a = 'name'
      b = say_hi()
  ```

  ```shell
   from aa import Foo   
   # 会打印出hi
  ```



  > 如何做？
  >
  > 将Category写成字符串，Python会通过反射或者其他方式去寻找到这个类，父级类的时候也可以这样用。

- choices

  ```python
  STATUS_ITEMS = (
  (1, '上线'),
  (2, '草稿'),
  (3, '删除')
  )
  
  # 像删除这类特殊操作可以选99这样的数字
  ```

- auto_now_add，当记录被创建时，会添加一条记录

- auto_now 每次修改时，会创建一条记录

- Class Meta

  - Verbose_name = verbose_name_plural = ' xxx '
  - 联合索引
  - 排序 ordering




Django.contrib属于贡献的代码，包括admin，属于非核心模块。

一般我们不做真正的删除操作，而是做标记删除。



## 字段的重写

- PositiveIntegerField
- BooleanField
- DataTimeField
- UrlField

这些字段是CharField的继承，在Django的层面做了加强，添加了一些限制，使用这些字段的一个好处是可以直接利用Django自带的验证。

对于Model来说，无论在哪个语言里都不可缺少，只要你用到ORM



## 创建Config

```shell
python manage.py startapp config
```

配置包含了侧边栏，友情链接，将来还可能包括其他东西

```python
class Link(models.Model):
	''''''
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重",
                                         help_text="权重越高展示顺序约靠前")
	''''''
```

有部分建模工具，可以直接生成Model层代码



migrations是你当前的model的版本记录，第三个是基于第二个，第二个基于第一个，对于协同工作，建议将migrations也提交上去。