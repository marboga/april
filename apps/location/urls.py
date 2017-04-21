from django.conf.urls import url

from . import views

app_name = 'location'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<id>\d+)$', views.show, name='show'),
    url(r'^name$', views.name, name='name'),
    url(r'^reset$', views.reset, name='reset'),
    url(r'^create$', views.create, name='create'),
    url(r'^create_stack$', views.create_stack, name='create_stack'),
    url(r'^add_stack$', views.add_stack, name='add_stack'),
    url(r'^splash$', views.splash, name='splash'),
]
