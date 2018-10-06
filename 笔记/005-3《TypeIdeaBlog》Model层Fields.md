# Fields字段



## 项目结构

我们通过Model之间的关系建立不同的app，对于我们以后的扩展来说这是一个比较好的根基，尤其是在团队协作中，也可通过这件事情来判断一个人的经验

如果你把model，form，views代码都写在同一个文件里，其他人来了它会按照你的痕迹在这个文件里不断添加东西，这样会导致文件越来越大，复杂度上升，可维护性越来越差。



## 字段

所有的Model都继承于models.Model，所有的字段对应的是数据库的字段

- CharField 对应 varchar
- ForeignKey 对应于 MySQL的integer，但其实实际业务中很少将外键约束建到数据库层，这样会对性能产生影响，一般在应用层面进行约束

- 所有的字段都继承自Field
- AutoField是id字段，自增主键
- CharField
- TextField
- URLField
- JsonField
- EmailField

基于对数据库的映射，做了一些应用层面的约束和检验



## ManyToManyField

多对多会产生三张表

两张基础表：Post, Tags

一张关联表：post_id, tag_id

through字段让你可以通过指定的中间表

```python
class PostTagsExtend(models.Model):
    post = models.ForeignKey("Post")
    tag = models.ForeignKey("Tag")
```



## 学Python基础两种方式

- 拿Python基础来不断练习
- 去看开源的代码，来检查自己对Python的掌握



## ORM

对象关系映射

一个是安全问题

一个是易用性问题

写：在通过Python对象映射到数据库表的过程中，我们可以做许多事情，比如安全验证，长度限制等等。

读：从数据库中取了数据，转换为字段后，可以通过一些属性来规定它的展示方式 



Model层的东西，可以在Form层进行重写