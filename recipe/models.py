from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.db import models

from django.db.models.functions import Concat
from django.contrib.gis.db import models as gis


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = ArrayField(models.CharField(max_length=100))
    instructions = models.JSONField()
    search_vector = SearchVectorField(null=True, blank=True)
    # Other fields of your recipe model
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Recipe.objects.filter(pk=self.pk).update(
            search_vector=SearchVector(
                Concat('title', 'ingredients', 'instructions',output_field=models.TextField())
            )
        )

    def __str__(self):
        return self.title

class Location(gis.Model):
    name = gis.CharField(max_length=100)
    coordinates = gis.PointField()


    def __str__(self):
        return self.name