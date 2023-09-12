from django.shortcuts import render, get_object_or_404
from .models import News


def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details_view(request, id):
    context = {"news": get_object_or_404(News, id=id)}
    return render(request, 'news_details.html', context)
