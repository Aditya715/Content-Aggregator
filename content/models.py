from django.db import models

# Create your models here.
class RealStateNews(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    url = models.URLField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.title

class RealStateArticle(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    url = models.URLField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.title