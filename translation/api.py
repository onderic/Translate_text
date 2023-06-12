from .models import Translation
from .serializers import TranslationSerializer
from rest_framework.response import Response



def get_translate(request):
    translate_text = Translation.objects.all()
    serializer = TranslationSerializer(translate_text, many=True)
    return Response(serializer.data)

