from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hexminton, name='index'),
    url(r'^$', views.hexminton, name='about'),
    url(r'^$', views.hexminton, name='contact'),

]
