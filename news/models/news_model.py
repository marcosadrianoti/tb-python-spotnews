from django.core.exceptions import ValidationError
from django.db import models


msg = ["Este campo não pode estar vazio."]


def is_one_word(title):
    if len(title.split(" ")) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        error_messages={"title": msg},
        validators=[is_one_word],
    )
    content = models.TextField(null=False, error_messages={"content": msg})
    author = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
        null=False,
        error_messages={"author": msg},
    )
    created_at = models.DateField(
        null=False, error_messages={"created_at": msg}
    )
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(
        "Categories", blank=False, null=False
    )

    def __str__(self):
        return self.title
