from django.conf.urls import include, url

from . import views

app_name = 'pha'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^study/(?P<phastudy_id>[0-9]+)/$', views.phaStudy, name='phaStudy'),
  
  
    url(r'^study/(?P<phaItem_id>[0-9]+)/$', views.phaItemDetail, name='phaItemDetail'),
    url(r'^(?P<phaItem_id>[0-9]+)/$', views.phaItemDetail, name='phaItemDetail'),
    url(r'^phaAction/$', views.phaActionList, name='phaActionList'),
    url(r'^(?P<phaAction_id>[0-9]+)/$', views.phaActionDetail, name='phaActionDetail'),
    ]