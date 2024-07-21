from django.db import models

# Create your models here.
class Collection(models.Model):
    Collection_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    Collcover = models.CharField(max_length=1000, default="img")

    def __str__(self):
        return self.Collection_name
class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    typ = models.CharField(max_length=200, default="article")
    artist = models.CharField(max_length=200)
    year = models.IntegerField()
    Piececover = models.CharField(max_length=1000, default="img")

    def __str__(self):
        return self.title