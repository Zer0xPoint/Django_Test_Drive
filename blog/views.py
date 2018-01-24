from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


# def post_list(request):  # request作为唯一参数，所有视图都需要
#     object_list = Post.published.all()  # 调用自制管理器 检索期望的Post
#     paginator = Paginator(object_list, 3)  # 设置每页有几个object
#     page = request.GET.get('page')  # 获取参数指明页数
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)  # 若page不是int型 则转到第一页
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)  # 若page超出范围 则转到最后一页
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts}, )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day, )  # 检索期望的Post
    return render(request,
                  'blog/post/detail.html',
                  {'post': post}, )  # 通过render渲染模版template


class PostListView(ListView):  # 基于类的视图
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
