from django.contrib import admin
from analyze_visual.models import Visual, StateInfo


class StateInfoInline(admin.TabularInline):
    model = StateInfo

class VisualAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'short_title', 'chart_type', 'image_url', 'order']
    list_editable = ['title', 'short_title', 'chart_type', 'image_url', 'order']
    inlines = [
        StateInfoInline,
    ]

admin.site.register(Visual, VisualAdmin)
admin.site.register(StateInfo)
# Register your models here.
