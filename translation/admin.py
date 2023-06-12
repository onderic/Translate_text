from django.contrib import admin
from .models import TranslationRequest,Translation

admin.site.register(TranslationRequest)


admin.site.register(Translation)