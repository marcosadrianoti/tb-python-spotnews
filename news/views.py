from django.shortcuts import render
from .models import News


def home(request):
    # news_list = News.objects.all()
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)
