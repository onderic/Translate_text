from django.db import models
from translate import Translator

class TranslationRequest(models.Model):
    text = models.TextField()
    language = models.CharField(max_length=50)

    def perform_translation(self):
        translator = Translator(to_lang=self.language)
        translation = translator.translate(self.text)
        return translation


class Translation(models.Model):
    source_text = models.TextField()
    translated_text = models.TextField()
    source_language = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.source_language}: {self.source_text} -> {self.translated_text}'
