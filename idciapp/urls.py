from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^paper/(?P<pk>\S+)/$', views.paperdetail, name='paperdetail'),
    url(r'^adsearch/?$', views.search, name='search'),
    #url(r'^search/', include('haystack.urls')),
    url(r'^search/', views.titlesearch, name='titlesearch'),

]
