from django.contrib import admin
from analyze_visual.models import Visual, StateInfo


class StateInfoInline(admin.TabularInline):
    model = StateInfo

class VisualAdmin(admin.ModelAdmin):
    inlines = [
        StateInfoInline,
    ]

admin.site.register(Visual, VisualAdmin)
admin.site.register(StateInfo)
# Register your models here.
