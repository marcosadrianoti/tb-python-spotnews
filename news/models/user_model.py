from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    role = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.name
