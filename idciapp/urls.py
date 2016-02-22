from django.conf.urls import include, url
from .views import CountryAutocomplete
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
    #url(r'^paper/(?P<pk>\S+)/$', views.paperdetail, name='paperdetail'),
    url(r'^paper/(?P<pk>\S+)/(?P<judul>.+)/$', views.paperdetail, name='paperdetail'),
    url(r'^author/(?P<nama>.+)/$', views.authorlist, name='authorlist'),
    url(r'^aff/(?P<nama>.+)/$', views.afflist, name='afflist'),
    url(r'^adsearch/?$', views.search, name='search'),
    #url(r'^search/', include('haystack.urls')),
    #url(r'^search/', views.titlesearch, name='titlesearch'),
    #url(r'^tsearch/(?P<judul>.+)$', views.titlesearch, name='titlesearch'),
    url(r'^tsearch/?$', views.titlesearch, name='titlesearch'),
    url(r'^asearch/?$', views.authorsearch, name='authorsearch'),
    url(r'^psearch/?$', views.publishersearch, name='publishersearch'),
    url('country-autocomplete/$',CountryAutocomplete.as_view(), name='country-autocomplete'),
    url(r'^list$', views.paperlist),

]
