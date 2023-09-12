from django.urls import path
from news.views import home, news_details_view, categories_form

urlpatterns = [
    path("", home, name="home-page"),
    path("<int:id>/", news_details_view, name="news-details-page"),
    path("categories/", categories_form, name='categories-form'),
]
