from django.db import models

# Create your models here.
class Alphabet(models.Model):
    character = models.CharField(max_length = 1)
    data = models.FileField(upload_to = 'Alphabet/')

    def __str__(self):
        return self.character

class Word(models.Model):
    word = models.CharField(max_length=100)
    data = models.FileField(upload_to = 'Word/')

    def __str__(self):
        return self.word
    