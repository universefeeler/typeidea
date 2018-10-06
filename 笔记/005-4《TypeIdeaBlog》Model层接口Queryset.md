# Model的接口Queryset



Django的Model层给我们提供了一套ORM机制

大家在意使用ORM时，在处理数据时会变得很慢，但ORM是可以优化的。



> #### 我们把Model层建好后，上层的所有查询都是通过Queryset来做的

在Model层中，Django通过给Model增加一个objects属性，来提供数据操作的接口。



## Queryset特点

#### 懒加载

你在写它的时候它并不会去使用数据库，它只会返回给你一个Queryset对象，只有在你真正使用它的时候它才会去操作数据库，比如print操作

```python
posts = Post.objects.all() # 返回一个Queryset对象
available_posts = posts.filter(status=1) # 返回一个Queryset对象
print(available_posts)	# 执行语句 select * from blog_post where status = 1;
```

#### 链式调用 

执行一个对象中的方法之后得到的结果，还是这个对象，可以接着执行对象上的其他方法。

```python
posts = Post.objects.filter(status=1).filter(category_id=2).flter(title__contains="xxx")
```

```python
class Queryset(object):
    def filter(self, *args):
        return self

    def all(self):
        return self


queryset = Queryset()

posts1 = queryset
posts2 = queryset.filter().all().filter()

print(posts1)
print(posts2)
print(posts1 == posts2)
```



#### Raw_data  ==>  filter1 ==> filter2 ==> filter3 ==> clean data



一个Queryset对应了多条查询结果

#### 支持链式调用的

- all()
- filter()
- exclude()
- reverse()
- distinct()
- none()



#### 不支持链式调用的接口

- get()
- create()
- get_or_create()  常用 
- update_or_create()
- count() 常用 
- latest()
- earlist()
- first()
- last()
- exisit()
- Bulk_create()
- in_bulk()
- update()



#### 进阶接口

- defer() 在里面填一个字段，告诉django这个字段我们不查，比如查询文章时，不查content
- only() 只查某个字段  select xxx from yyy
- select_related() 
- Prefetch_related()



## ORM优化

defer( ) 避开数据量大的字段, only()只查指定字段

```python
post = Post.objects.all().defer('content') ==> select id, title from blog_post;
poss = Post.objects.all().only('title') ==> select title from blog_post;
```



## 通过TestCase进行查询

```python
# Create your tests here.

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase

from .models import Category


class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('huangke', 'kwell@163.com', 'password')
        for i in range(10):
            category_name = 'cate_%s' % i
            Category.objects.create(name=category_name, owner=user)

    def test_filter(self):
        categories = Category.objects.all()
        print(categories.query)  # 要执行的SQL语句
        categories = categories.filter(status=1)
        print(categories.query)
        print(connection.queries)
        print(len(categories))
```

```shell
python manage.py test blog
```

结果

```shell
# categories = Category.objects.all()
# print(categories.query)  # 要执行的SQL语句
SELECT "blog_category"."id", "blog_category"."name", "blog_category"."status", "blog_category"."is_nav", "blog_category"."owner_id", "blog_category"."created_time" FROM "blog_category"

# categories = categories.filter(status=1)
# print(categories.query)
SELECT "blog_category"."id", "blog_category"."name", "blog_category"."status", "blog_category"."is_nav", "blog_category"."owner_id", "blog_category"."created_time" FROM "blog_category" WHERE "blog_category"."status" = 1

# print(connection.queries)
[]

# print(len(categories))
10
```

