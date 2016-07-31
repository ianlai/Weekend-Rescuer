from django.conf.urls import url

from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.TasklistView.as_view(), name='tasklist'),
    url(r'^add/$', views.get_newtask, name='add'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
