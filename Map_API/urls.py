from django.conf.urls import url
from Map_API import views

urlpatterns = [
        url(r'^$', views.mapLoad, name='Login page'),#Login api url
        url(r'^address_Data/$',views.addressService, name='address_service'),
    
      ]