from django import forms

from news.models.category_model import Categories


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
