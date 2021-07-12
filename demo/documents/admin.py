from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentsAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
