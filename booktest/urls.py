from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^$', views.index),
    url(r'^details/(\d)$', views.details),
    url(r'^area/$', views.area, name='area'),


]