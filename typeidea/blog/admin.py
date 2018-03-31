from django.contrib import admin
from typeidea.custom_site import custom_site

# Register your models here.


from django.contrib import admin
from .models import Post, Category, Tag
from django.utils.html import format_html
from django.urls import reverse


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


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Post)
admin.sites.site.register(Post)
