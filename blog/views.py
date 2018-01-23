from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()  # 调用自制管理器
    return render(request,
                  'blog/post/list.html',
                  {'post': posts}, )


def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day, )  # 检索期望的Post
    return render(request,
                  'blog/post/detail.html',
                  {'post': post}, )  # 建立模版Template
