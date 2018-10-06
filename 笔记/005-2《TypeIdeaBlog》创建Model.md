通过commit，我们每次提交的内容都是记录在案的

在一个完整的项目中，可能有不同的app，每个app是你抽象出来的一部分业务，这部分业务可能关联性比较强，就把它放在一个app里面，如果关联性不强，就放在不同的app中。

TypeIdea的app划分是通过模型来进行划分的



## 创建模型

对一个模型的CharField，在Python里中文默认使用unicode，而在MySQL中是用的utf-8，

- max_length对应的是数据库中的varchar()
- blank默认为False，如果为True则可以为空
- Verbose_name是后台显示名称

#### ForeignKey()

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

将Category写成字符串，Python会通过反射或者其他方式去寻找到这个类，父级类的时候也可以这样用。



