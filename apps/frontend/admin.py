from apps.frontend.models import Page, News, Developer, FrontendImage
from django.contrib import admin


class InlineImage(admin.TabularInline):
    model = FrontendImage


class DeveloperAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Page)
admin.site.register(News)
admin.site.register(Developer, DeveloperAdmin)
