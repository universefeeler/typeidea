# Queryset 常用API



Unresolved attribute reference 'objects' for class 'Category'

在Pycharm中 Language&Framework里enable django support



当我们拿到一个Queryset时，如果我们不用它，它是不会hit db的

**对于Queryset每一条代码，你需要知道它是在Python层面执行还是在数据库层面执行，否则难言优化。**



## 查询优化示例



#### 原始查询		(3次hit db)

```python
    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.all()
        if categories.count() == 0:		# 此处使用count()会导致一次查询，hit db
            return

        categories = categories.filter(status=1)
        for cate in categories:
            print(cate)
            
        categories = categories.filter(status=0)
        for cate in categories:
            print(cate)
```





#### 使用列表推导式	(2次hit db)

第一次优化，使用 queryset 代替 queryset.count()，只在Python层面判断

```python
    @override_settings(DEBUG=True)
    def test_filter(self):
        queryset = Category.objects.all()
        if not queryset:
            return

        available_categories = [cate for cate in queryset if cate.status == 1]
        for cate in available_categories:
            print(cate)

        categories = [cate for cate in queryset if cate.status == 0]
        for cate in categories:
            print(cate)
```

上面虽然用了列表推导式，但是循环了4次，将其优化为1次遍历 



#### 优化版，一次遍历

```python
    @override_settings(DEBUG=True)
    def test_filter(self):
        queryset = Category.objects.all()
        if not queryset.count():
            return

        available_categories = []
        categories = []
        for cate in queryset:
            if cate.status == 1:
                available_categories.append(cate)
            else:
                categories.append(cate)
```





## 常用API

objects是Manager

#### 链式调用接口

- all()	查询所有

- filter()  查询过滤

- exclude()  查询排除

- distinct() 查询去重

- none() 返回一个空的queryset

- order_by() 查询排序，取负号时逆序

- ```python
  categories = queryset.order_by('?')
  # 随机排序
  ```

#### 非链式

- get() 只返回一个，如果有多个满足条件就会报错

- create()

- get_or_create()，返回一个元组

  ```python
  cate, is_created = Category.objects.get_or_create(name='django', owner=self.user)
  print(cate)
  print(is_created)
  ```

- update_or_create() 同上

- count()

- latest() 查询最新的一个

- ealiest()查询最早的一个

  ```python
  cate = Category.objects.latest('created_time')
  ```

- first() 按id来排序取第一个

- last() 按id来排序取最后一个

- exists() 取limit=1的一个

  ```python
  cate = Category.objects.exists()
  print(cate)
  print(connection.queries)
          
  True
  [{'sql': 'SELECT (1) AS "a" FROM "blog_category" LIMIT 1', 'time': '0.000'}]
  ```

- bulk_create() 批量插入，更快更方便

- update() 批量修改