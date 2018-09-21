---
title: 《TypeIdeaBlog_6_4》  定制admin后台
date: 2018-04-02 23:53:00
tags:
	- Django
	- TypeIdeaBlog
---



## 定制后的PostAdmin

```python
@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'show_status', 'status', 'owner', 'created_time', 'operator', 'delete_post')
    search_fields = ['title', 'category__name', 'owner__username']
    list_filter = ('owner',)
    save_on_top = True
    show_full_result_count = True
    list_display_links = ['title', ]
    actions_on_bottom = True
    actions_on_top = True
    list_editable = ('status', 'category', 'owner')
    filter_horizontal = ('tags',)
    
    fieldsets = (
        ('基础设置', {
            'fields': (('title', 'category'), 'status', 'content')
        }),
        ('高级选项', {
            'classes': ('collapse', 'addon', 'wide', 'extrapretty'),
            'fields': ('tags',),
        }),
    )
    
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    
    def delete_post(self, obj):
        return format_html(
            '<a href="{}">删除</a>',
            reverse('cus_admin:blog_post_delete', args=(obj.id,))
        )
    
    operator.short_description = '操作'
    delete_post.short_description = '删除'
```



## 重写字段

```python
    list_display = ('title', 'category', 'show_status', 'status', 'owner', 
                    'created_time', 'operator', 'delete_post')
    search_fields = ['title', 'category__name', 'owner__username']
    list_filter = ('owner',)
    save_on_top = True
    show_full_result_count = True
    list_display_links = ['title', ]
    actions_on_bottom = True
    actions_on_top = True
    list_editable = ('status', 'category', 'owner')
    filter_horizontal = ('tags',)
```

ModelAdmin里的字段都可以重写，具体查询django文档 



## 编辑页面定制布局

```python
    fieldsets = (
        ('基础设置', {
            'fields': (('title', 'category'), 'status', 'content')
        }),
        ('高级选项', {
            'classes': ('collapse', 'addon', 'wide', 'extrapretty'),
            'fields': ('tags',),
        }),
    )
```

fieldsets可以进行高级布局，比如上述代码，将界面分为 基础设置 和 高级选项 两块

fields表示要展示的字段，可以通过tuple把两个字段展示在同一行

classes表示此块的class属性，比如collapse表示收缩



## 列表页面定制按钮



#### 在admin.py文件里定制

```python
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    
    def delete_post(self, obj):
        return format_html(
            '<a href="{}">删除</a>',
            reverse('cus_admin:blog_post_delete', args=(obj.id,))
        )
    
    operator.short_description = '操作'
    delete_post.short_description = '删除'
```



#### 在models.py文件里定制

```python
    def show_status(self):
        return '当前状态: %s' % self.status
    
    show_status.short_description = '展示状态'
```



在两处定制是效果是一样的