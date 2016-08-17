from django.conf.urls import url

from . import views

app_name='todo'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'), 
    ]

# name='xxx' is not necessary the same as views.yyy (tested)
