from django.conf import settings
from django.conf.urls import include, url

from .feeds import PostFeed

from . import views

from .views import BlogPostAdd


urlpatterns = [
    
    url(r'^$', views.pageone),
    url(r'^signuser/(?P<idn>\d+)$', views.pagetwo),
    url(r'^write/(?P<idn>\d+)$', views.postwrite),
    url(r'^addpost/$', BlogPostAdd.as_view()),
    url(r'^logout/$', views.logout_view),
    url(r'^feed/$', PostFeed()),

]


