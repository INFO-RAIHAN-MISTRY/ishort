from django.contrib import admin
from functions.models import (
    Url
)
# Register your models here.

@admin.register(Url)
class UrlAdminView(admin.ModelAdmin):
    list_display = [
        'user',
        'short_url',
        'long_url',
        'url_title',
        'url_hit_count',
        'url_created_at',
        'url_updated_at',
    ]