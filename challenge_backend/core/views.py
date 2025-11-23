from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import Trainer, Pokemon, TrainerPokemon
from .serializers import TrainerSerializer, PokemonSerializer, TrainerPokemonSerializer   

class TrainerListCreateView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer    


class TrainerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer



class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TrainerPokemonCreateView(generics.CreateAPIView): 
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer


class TrainerPokemonDeleteView(generics.RetrieveDestroyAPIView):    
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer


class PokeAPIView(APIView):
    def get(self, request, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"

        response = requests.get(url)

        if response.status_code == 200:
            return Response(
                {"error": "Pokémon não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = response.json()

        pokemon_data = {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "photo": data["sprites"]["front_default"],
        }

        return Response(pokemon_data, status=status.HTTP_200_OK)