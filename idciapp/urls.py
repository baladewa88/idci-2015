from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^paper/(?P<pk>\S+)/$', views.paperdetail, name='paperdetail'),
]
