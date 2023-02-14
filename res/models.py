from django.db import models

# Create your models here.


class Todos(models.Model):
    text = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class Menu(models.Model):
    to = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    private = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.to, self.text


class Post(models.Model):
    auth = models.CharField(max_length=45)
    content = models.TextField(max_length=245)
    slug = models.CharField(max_length=45)
    title = models.CharField(max_length=50)

    def __str__(self):
        return (self.auth, self.content, self.slug, self.title)