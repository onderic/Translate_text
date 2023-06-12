import json
from django.core.management.base import BaseCommand
from translation.models import Translation
import os


class Command(BaseCommand):
    help = 'Populate translations in the database'

    def handle(self, *args, **options):
        json_path = os.path.join(os.getcwd(), 'translations.json')
        with open(json_path, 'r') as f:
            translations = json.load(f)

        for translation in translations:
            Translation.objects.create(
                source_language=translation['code'],
                target_language=translation['name'],
                source_text=translation['words'][0],
                translated_text=""
            )
