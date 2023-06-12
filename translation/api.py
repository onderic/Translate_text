from rest_framework.decorators import api_view
from .models import TranslationRequest, Translation
import json
from django.http import JsonResponse


@api_view(['POST'])
def translate(request):
    if request.method == "POST":
        text = request.data.get("translate")
        language = request.data.get("language")

        translation_request = TranslationRequest(text=text, language=language)
        translation = translation_request.perform_translation()

        
        #Optional to Create a new instance of Translation model
        translation_obj = Translation(source_text=text, translated_text=translation, source_language=language)

        # Save the translation object to the database
        translation_obj.save()

        return JsonResponse({"translation": translation})
