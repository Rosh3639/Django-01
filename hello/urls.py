

from django.urls import path
from hello import views

urlpatterns = [
    path('', views.index, name='hello'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]


