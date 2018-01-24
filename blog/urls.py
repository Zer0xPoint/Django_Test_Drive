from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # blog/页面映射到post_list视图
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',  # url由一个正则+一个view+一个全项目范围内的name构成
        views.post_detail,
        name='post_detail', ),  # blog/日期/slug/页面映射到post_detail视图
]
