from django.urls import path
from Galaxy_Website import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('home/', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('documentschecklist/', views.documentschecklist,name="documentschecklist"),
    path('about/', views.about, name="about"),
    path('contact/',views.contact, name="contact")
]