from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hexminton, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^player/(\d+)', views.player_details, name='player_details'),

]
