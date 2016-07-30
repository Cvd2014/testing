from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blogviews

urlpatterns = [
    # Examples:
    # url(r'^$', 'blogmodule.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', blogviews.post_list)
]
