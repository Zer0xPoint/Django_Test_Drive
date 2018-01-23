from django.conf.urls import url, include
from blog import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls',
                           namespace='blog',
                           app_name='blog')),
]
