from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.home, name='about'),
    url(r'^portfolio/$', views.home, name='portfolio'),
    url(r'^contact/$', views.home, name='contact'),
    url(r'^resume/$', views.resume, name='resume'),
    ]