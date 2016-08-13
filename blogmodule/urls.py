from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT

urlpatterns = [
    # Examples:
    # url(r'^$', 'blogmodule.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('blog.urls')),
    url(r'^$', include('homepage.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':MEDIA_ROOT}),
    url(r'',include('articles.urls'))
]
