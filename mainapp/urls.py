from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.work_list, name='work_list'),
    url(r'^work/(?P<pk>\d+)/$', views.work_detail, name='work_detail'),
    url(r'^work/new/$', views.work_new, name='work_new'),
    url(r'^work/(?P<pk>\d+)/edit/$', views.work_edit, name='work_edit'),
]
