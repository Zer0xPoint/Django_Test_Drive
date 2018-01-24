from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)  # 控制显示属性
    list_filter = ('status', 'created', 'publish', 'author',)  # 控制过滤器内容
    search_fields = ('title', 'body',)  # 控制搜索栏
    prepopulated_fields = {'slug': ('title',)}   # 控制Post时使Slug同步title
    raw_id_fields = ('author',)  # 控制Post时使用用户ID
    date_hierarchy = 'publish'  # 控制时间层导航
    ordering = ['status', 'publish']  # 控制排序


admin.site.register(Post, PostAdmin, )