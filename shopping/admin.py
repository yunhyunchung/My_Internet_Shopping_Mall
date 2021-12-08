from django.contrib import admin
from .models import Piano, Maker, Category
from markdownx.admin import MarkdownxModelAdmin

# 관리자 페이지에 Piano 등록, Markdown(적용한 preview) 등록
admin.site.register(Piano, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
class MakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Maker, MakerAdmin)
