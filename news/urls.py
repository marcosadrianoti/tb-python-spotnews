from django.urls import path
from news.views import home, news_details_view, categories_form, news_form, creat_new

urlpatterns = [
    path("", home, name="home-page"),
    path("<int:id>/", news_details_view, name="news-details-page"),
    path("categories/", categories_form, name='categories-form'),
    path("news/", news_form, name="news-form"),
    path("teste/", creat_new, name="news-form2"),
]
