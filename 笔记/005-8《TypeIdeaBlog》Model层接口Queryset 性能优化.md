# Queryset 性能优化





## values

只取指定字段的值，也是性能优化的一部分

```python
    def test_values(self):
        cates = Category.objects.values('name')
        print(cates)
        print(type(cates))
```

结果

```shell
<QuerySet [{'id': 1, 'name': 'cate_0'}, {'id': 2, 'name': 'cate_1'}, {'id': 3, 'name': 'cate_2'}, {'id': 4, 'name': 'cate_3'}, {'id': 5, 'name': 'cate_4'}, {'id': 6, 'name': 'cate_5'}, {'id': 7, 'name': 'cate_6'}, {'id': 8, 'name': 'cate_7'}, {'id': 9, 'name': 'cate_8'}, {'id': 10, 'name': 'cate_9'}]>
```



## Values_list

```python
    def test_values(self):
        catelist = Category.objects.values_list('name') # 返回元组
        catelist = Category.objects.values_list('name', flat=True) # 返回列表 
        print(catelist)
```



```shell
<QuerySet [('cate_0',), ('cate_1',), ('cate_2',), ('cate_3',), ('cate_4',), ('cate_5',), ('cate_6',), ('cate_7',), ('cate_8',), ('cate_9',)]>
Destroying test database for alias 'default'...
```



## 先做性能分析

工具

- django.db.connection
- django_debug_toolbar

前者用于查看详细的SQL执行过程 

后者会告诉你的各种执行时间

#### 标准数据库优化技巧

加索引字段



## 理解Queryset求值过程

- Queryset是惰性的

  ```python
  news_list = News.object.all()
  # 此时并未执行数据库查询操作
  print(news_list) 
  # 此时执行查询
  ```

- 数据如何被缓存？

  ```python
  print([e.headline for e in Entry.objects.all()])
  print([e.head_date for e in Entry.objects.all()])
  # 此时并未被缓存，因为没有生成queryset对象
  
  entries = Entry.objects.all()
  print([e.headline for e in entries])
  # 此时被缓存
  ```


理解被缓存的属性

- Queryset会被缓存

  如果你不把它赋值成一个Queryset，它就无法被缓存

- 不可被调用的属性会被缓存

  ```python
  news = News.objects.get(id=1)
  news.channel	# 此时从数据库查询
  news.channel 	# 此时是从缓存中查询
  ```

- 方法的调用每次都会触发数据库查询

  ```python
  news = News.objects.get(id=1)
  news.authors.all()	# 此时从数据库查询
  news.authors.all() 	# 再次从数据库查询
  ```


#### 数据量非常大时，使用iterator()

```python
news_list = News.objects.filter(title__contains="xxx")
for news in news_list.iterator():
    print(news)
```



#### 使用原生的SQL

```python
cl = Channel.objects.raw('SELECT * FROM web_channel WHERE parent_id = 1')
print(cl)
```



#### 查询数量

使用queryset.count()而不要用len(queryset)



#### 查询存在

使用queryset.exists()不要用 if queryset: