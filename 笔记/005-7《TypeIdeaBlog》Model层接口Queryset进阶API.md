# Queryset 进阶API



进阶接口，新手写完代码后，审核时可能会指出，这个代码有问题，去看xxx API



## defer() 

#### 排除某些字段

https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.query.QuerySet.defer)

This is done by passing the names of the fields to not load to `defer()`:

比如查询posts文章，文章主体含有大量数据，不适合包含在查询中，用defer来排除

```
Entry.objects.defer("headline", "body")
```

```python
def test_filter(self):
    cate = Category.objects.filter(status=1).defer('created_time')
    print(cate)
    print(connection.queries)
```

具体执行的操作

```shell
[{'sql': 'SELECT "blog_category"."id", "blog_category"."name", "blog_category"."status", "blog_category"."is_nav", "blog_category"."owner_id" FROM "blog_category" WHERE "blog_category"."status" = 1 ORDER BY "blog_category"."id" ASC, "blog_category"."created_time" ASC LIMIT 21', 'time': '0.000'}]
Destroying test database for alias 'default'...
```



## only()

只取某些字段 

https://docs.djangoproject.com/en/2.1/ref/models/querysets/#only

The `only()` method is more or less the opposite of [`defer()`](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.query.QuerySet.defer). You call it with the fields that should *not* be deferred when retrieving a model. If you have a model where almost all the fields need to be deferred, using `only()` to specify the complementary set of fields can result in simpler code.

Suppose you have a model with fields `name`, `age` and `biography`. The following two querysets are the same, in terms of deferred fields:

```
Person.objects.defer("age", "biography")
Person.objects.only("name")
```

```python
cates = Category.objects.filter(status=1).only('created_time')
print(cates)
print(connection.queries)
```

具体执行的操作

```shell
[{'sql': 'SELECT "blog_category"."id", "blog_category"."created_time" FROM "blog_category" WHERE "blog_category"."status" = 1 ORDER BY "blog_category"."id" ASC, "blog_category"."created_time" ASC LIMIT 21', 'time': '0.000'}]
```



## Select_related()

#### 解决外键的查询

未使用select_related()优化

```python
def test_filter(self):
    cates = Category.objects.filter(status=1)
    for cate in cates:
        print(cate.owner)

    print(connection.queries)
```

输出

```python
[{'sql': 'SELECT "blog_category"."id", "blog_category"."name", "blog_category"."status", "blog_category"."is_nav", "blog_category"."owner_id", "blog_category"."created_time" FROM "blog_category" WHERE "blog_category"."status" = 1 ORDER BY "blog_category"."id" ASC, "blog_category"."created_time" ASC', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}, {'sql': 'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1', 'time': '0.000'}]
Destroying test database for alias 'default'...
```

执行了很多条SQL语句，负担极重

#### 使用select_related()

```python
    def test_filter(self):
        cates = Category.objects.filter(status=1).select_related('owner')
        for cate in cates:
            print(cate.owner)

        print(connection.queries)
```



```shell
[{'sql': 'SELECT "blog_category"."id", "blog_category"."name", "blog_category"."status", "blog_category"."is_nav", "blog_category"."owner_id", "blog_category"."created_time", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined"

FROM "blog_category" INNER JOIN "auth_user" 
ON ("blog_category"."owner_id" = "auth_user"."id") 
WHERE 
"blog_category"."status" = 1 
ORDER BY "blog_category"."id" ASC, "blog_category"."created_time" ASC', 'time': '0.000'}]
Destroying test database for alias 'default'...
```

执行了一条inner join查询语句，大大优化



参考： [科普文]什么是ORM中的N+1

https://www.the5fire.com/what-is-orm-n+1.html



## Prefetch_related()

解决的是ManyToMany()的查询问题





## 进阶Lookup表达式



## Q 

条件语句

```python
    def test_filter(self):
        cates = Category.objects.filter(
            Q(id=1) | Q(id=2)
        )
        for cate in cates:
            print(cate)
            
    #    Q(id=1) & Q(id=2)
```



## F

处理并发，防止竞争，可以使用F来进行更新。

```python
# 错误写法
cat.status = cat.status + 1

# 改写
cat.status = F('status') + 1
# 或
cat = Category.objects.filter(id=1).update(status=F('status') + 1)
```



## Count

查询数量

```python
users = User.objects.filter(username='huangke')
user = users[0]
n = user.category_set.count()
print(n)
print(connection.queries)
```



## Annotate

动态给类创建一个属性，相当于SQL中的 as 取别名

```python
users = User.objects.filter(username='huangke').annotate(cate_count=Count('category'))
user = users[0]
# n = user.category_set.count()
n = user.cate_count
print(n)
print(connection.queries)
```

