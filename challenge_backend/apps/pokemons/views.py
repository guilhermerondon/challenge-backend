import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonCreateView(APIView):
    def post(self, request):
        name = request.data.get("name")

        if not name:
            return Response({"erro": "O campo 'name' é obrigatório."}, status=400)

        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

        response = requests.get(url)

        if response.status_code != 200:
            return Response({"erro": "Pokémon não encontrado na PokeAPI."}, status=404)

        data = response.json()

        pokemon = Pokemon.objects.create(
            name=name.capitalize(),
            image=data["sprites"]["front_default"],
            height=data["height"],
            weight=data["weight"],
        )

        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data, status=201)
    
    
class PokemonListView(APIView):
    def get(self, request):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)
    

class PokemonDetailView(APIView):
    def get_object(self, pk):
        try:
            return Pokemon.objects.get(pk=pk)
        except Pokemon.DoesNotExist:
            return None

    def get(self, request, pk):
        pokemon = self.get_object(pk)
        if not pokemon:
            return Response({"erro": "Pokémon não encontrado."}, status=404)

        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    def patch(self, request, pk):
        pokemon = self.get_object(pk)
        if not pokemon:
            return Response({"erro": "Pokémon não encontrado."}, status=404)

        serializer = PokemonSerializer(pokemon, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        pokemon = self.get_object(pk)
        if not pokemon:
            return Response({"erro": "Pokémon não encontrado."}, status=404)

        pokemon.delete()
        return Response(status=204)
