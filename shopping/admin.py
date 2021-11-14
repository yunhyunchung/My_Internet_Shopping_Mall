from django.contrib import admin
from .models import Piano, Maker, Category
# Register your models here.

admin.site.register(Piano)
admin.site.register(Maker)
admin.site.register(Category)
