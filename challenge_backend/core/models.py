from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()
    height = models.IntegerField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TrainerPokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('trainer', 'pokemon')
                                           

    def __str__(self):
        return f"{self.trainer.name} -> {self.pokemon.name}"