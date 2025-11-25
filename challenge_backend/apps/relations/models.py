from django.db import models
from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon

class TrainerPokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="pokemons")
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('trainer', 'pokemon')

    def __str__(self):
        return f"{self.trainer.name} - {self.pokemon.name}"
