from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # 标题
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # 短标签
    author = models.ForeignKey(User, related_name='blog_post')  # 关联User模型
    body = models.TextField()  # 主体
    publish = models.DateTimeField(default=timezone.now)  # 发布时间
    created = models.DateTimeField(auto_now_add=True)  # 更新时间
    update = models.DateTimeField(auto_now=True)  # 创建时间
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')   # 当前状态

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
