# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.db import models

# from django.db.models.functions import Concat
# from django.contrib.gis.db import models as gis


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
#     search_vector = SearchVectorField(null=True, blank=True)
    
#     # def save(self, *args, **kwargs):
#     #     super().save(*args, **kwargs)
#     #     Recipe.objects.filter(pk=self.pk).update(
#     #         search_vector=SearchVector(
#     #             Concat('title', 'ingredients', 'instructions',output_field=models.TextField())
#     #         )
#     #     )
    class Meta:
        indexes = [models.Index(fields=['name', 'ingredients','instructions'])]

    def __str__(self):
        return self.name
