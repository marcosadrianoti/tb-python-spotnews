from django import forms

from news.models.category_model import Categories
from news.models.news_model import News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'author': forms.Select(),
        }
