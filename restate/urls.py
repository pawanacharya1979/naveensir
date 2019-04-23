from django.conf.urls import url
from . import views

urlpatterns = [
         url(r'^$', views.home, name='home'),
         url(r'^projects/$', views.project, name='project'),
         url(r'^contact/$', views.contactus, name='contactus'),
         url(r'^nri-corner/$', views.nricorner, name='nricorner'),
         url(r'^about-us/$', views.aboutestate, name='aboutestate'),
       ]