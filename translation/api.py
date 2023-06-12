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

        print("Translation:", translation)

        # Optional to create a new instance of Translation model
        # translation_obj = Translation(source_text=text, translated_text=translation, source_language=language)
        # translation_obj.save()

        # print("Translation saved to database")

        return JsonResponse({"translation": translation})
