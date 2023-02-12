from django.db import models

# Create your models here.


class Todos(models.Model):
  text = models.CharField(max_length=50, null=True)
  completed = models.BooleanField(default=False)
  create_at = models.DateTimeField(auto_now_add=True)