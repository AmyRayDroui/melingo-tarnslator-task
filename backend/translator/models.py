from django.db import models

class Entry(models.Model):
    MelingoId = models.IntegerField(primary_key=True)
    Entry = models.CharField(max_length=255)
    TranslationFull = models.CharField(max_length=255)

class Example(models.Model):
    ID = models.IntegerField(primary_key=True)
    MelingoId = models.ForeignKey(Entry, on_delete=models.CASCADE, to_field='MelingoId', related_name='examples' )
    Text = models.CharField(max_length=500)