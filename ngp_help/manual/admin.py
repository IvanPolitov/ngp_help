from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Manual, Category


admin.site.register(Manual)
admin.site.register(Category)
