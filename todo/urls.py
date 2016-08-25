from django.conf.urls import url

from . import views

# app_name='todo'
# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^index/$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'), 
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), 
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), 
#     ]


app_name='todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/',          views.detail,  name='detail'), 
    url(r'^(?P<question_id>[0-9]+)/vote/$',    views.vote,    name='vote'), 
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'), 
    ]




# name='xxx' is not necessary the same as views.yyy (tested)
