from django.urls import path
from news.views import home

urlpatterns = [
    path("", home, name="home-page"),
]
