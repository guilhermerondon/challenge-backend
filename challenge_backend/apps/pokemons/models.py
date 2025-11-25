from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
