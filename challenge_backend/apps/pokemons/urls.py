from django.urls import path
from .views import PokemonCreateView, PokemonListView, PokemonDetailView

urlpatterns = [
    path("", PokemonListView.as_view(), name="pokemon-list"),
    path("create/", PokemonCreateView.as_view(), name="pokemon-create"),
    path("<int:pk>/", PokemonDetailView.as_view(), name="pokemon-detail"),
]
