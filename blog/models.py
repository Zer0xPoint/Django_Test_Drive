from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')  # 自制管理器


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
    object = models.Manager()  # 默认管理器
    published = PublishedManager()  # 自建的管理器

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-publish',)  # 按发布时间倒序排序

    def __str__(self):
        return self.title
