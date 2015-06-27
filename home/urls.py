from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^login/$', 'blog.views.user_login', name='login'),
    url(r'^logout/$', 'blog.views.user_logout', name='logout'),
    url(r'^addPost/$', 'blog.views.add_post', name='addPost'),
    url(r'^post/like/$', 'blog.views.like_post', name='like_post'),
)
