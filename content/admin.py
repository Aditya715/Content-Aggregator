from django.contrib import admin
from .models import (
    RealStateNews,
    RealStateArticle,
)

# Register your models here.
admin.site.register(RealStateNews)
admin.site.register(RealStateArticle)