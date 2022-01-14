from django.urls import path
from phishing import views

urlpatterns = [
    path('', views.index, name="home"),
    path('facebook', views.fb, name="fb"),
    path('instagram', views.insta, name="insta")
]
