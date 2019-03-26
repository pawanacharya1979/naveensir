from django.conf.urls import url
from . import views

urlpatterns = [
         url(r'^$', views.home, name='home'),
         url(r'^aboutus/$', views.about, name='about'),
         url(r'^contact/$', views.contactus, name='contactus'),

       ]