from django.contrib import admin

from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'subheading_1', 'subheading_2')
    search_fields = ('title', 'subheading_1', 'subheading_2')