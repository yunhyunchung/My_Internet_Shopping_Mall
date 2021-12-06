from django.contrib import admin
from .models import Piano, Maker, Category
# Register your models here.

admin.site.register(Piano)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
class MakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Maker, MakerAdmin)
