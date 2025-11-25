from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.trainers.models import Trainer
from apps.pokemons.models import Pokemon
from .models import TrainerPokemon
from .serializers import TrainerPokemonSerializer

class AddPokemonToTrainerView(APIView):
    def post(self, request, trainer_id, pokemon_id):
        # Verificar se trainer existe
        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except Trainer.DoesNotExist:
            return Response({"erro": "Treinador não encontrado."}, status=404)

        # Verificar se pokemon existe
        try:
            pokemon = Pokemon.objects.get(id=pokemon_id)
        except Pokemon.DoesNotExist:
            return Response({"erro": "Pokémon não encontrado."}, status=404)

        # Evitar duplicação
        if TrainerPokemon.objects.filter(trainer=trainer, pokemon=pokemon).exists():
            return Response({"erro": "Este Pokémon já está associado ao treinador."}, status=400)

        relation = TrainerPokemon.objects.create(trainer=trainer, pokemon=pokemon)
        serializer = TrainerPokemonSerializer(relation)

        return Response(serializer.data, status=201)
    

    

class RemovePokemonFromTrainerView(APIView):
    def delete(self, request, trainer_id, pokemon_id):
        # Verificar se a relação existe
        from .models import TrainerPokemon

        try:
            relation = TrainerPokemon.objects.get(trainer_id=trainer_id, pokemon_id=pokemon_id)
        except TrainerPokemon.DoesNotExist:
            return Response(
                {"erro": "Este Pokémon não está associado a este treinador."},
                status=404
            )

        relation.delete()
        return Response({"mensagem": "Pokémon removido do treinador com sucesso."}, status=200)
