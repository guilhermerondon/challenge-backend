from django.urls import path
from .views import (
  TrainerListCreateView, PokemonListCreateView, TrainerPokemonCreateView, TrainerDetailView, PokemonDetailView, TrainerPokemonDeleteView, PokeAPIView, PokemonBattleView
)

urlpatterns = [
    path('trainers/', TrainerListCreateView.as_view()),
    path('trainers/<int:pk>/', TrainerDetailView.as_view()),

    path('pokemons/', PokemonListCreateView.as_view()),
    path('pokemons/<int:pk>/', PokemonDetailView.as_view()),    

    path('trainer-pokemons/', TrainerPokemonCreateView.as_view()),
    path('trainer-pokemons/<int:pk>/', TrainerPokemonDeleteView.as_view()),

    path('pokeapi/<str:pokemon_name>/', PokeAPIView.as_view()),

    path('battle/<int:pokemon1_id>/<int:pokemon2_id>/', PokemonBattleView.as_view()),
]  