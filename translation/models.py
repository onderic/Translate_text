from django.db import models

class Translation(models.Model):
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    source_text = models.TextField()
    translated_text = models.TextField()

    def __str__(self):
        return f'{self.source_language} to {self.target_language}'
