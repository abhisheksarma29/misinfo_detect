from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    url(r'^$',views.search,name='search')]
  #  urlpatterns += staticfiles_urlpatterns()