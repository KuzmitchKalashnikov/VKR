from django.contrib import admin
from .models import PlantQuery


@admin.register(PlantQuery)
class PlantQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'short_result')
    list_filter = ('created_at', 'user')
    search_fields = ('result', 'user__username')
    readonly_fields = ('image_preview',)

    def short_result(self, obj):
        return obj.result[:50] + '...' if len(obj.result) > 50 else obj.result

    def image_preview(self, obj):
        return obj.image.url if obj.image else 'No Image'

    short_result.short_description = 'Result'
    image_preview.short_description = 'Image Preview'
