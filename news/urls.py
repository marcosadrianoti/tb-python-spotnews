from django.urls import path
from news.views import home, news_details_view

urlpatterns = [
    path("", home, name="home-page"),
    path("<int:id>/", news_details_view, name="news-details-page"),
]
