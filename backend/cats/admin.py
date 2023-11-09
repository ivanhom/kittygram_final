from django.contrib import admin

from .models import Achievement, Cat

admin.site.empty_value_display = 'Не задано'


class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner')
    search_fields = ('name', 'birth_year', 'owner')
    list_display_links = ('name',)
    list_filter = ('color', 'birth_year', 'owner')


admin.site.register(Achievement)
admin.site.register(Cat, CatAdmin)
