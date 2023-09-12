from django.shortcuts import redirect, render, get_object_or_404

from news.forms import CategoryForm
from .models import News


def home(request):
    context = {"all_news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details_view(request, id):
    context = {"news": get_object_or_404(News, id=id)}
    return render(request, 'news_details.html', context)


def categories_form(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    return render(request, 'categories_form.html', {'form': form})
