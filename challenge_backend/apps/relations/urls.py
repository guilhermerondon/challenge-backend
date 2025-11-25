from django.urls import path
from .views import AddPokemonToTrainerView
from .views import RemovePokemonFromTrainerView

urlpatterns = [
    path('add/<int:trainer_id>/<int:pokemon_id>/', AddPokemonToTrainerView.as_view()),
    path('remove/<int:trainer_id>/<int:pokemon_id>/', RemovePokemonFromTrainerView.as_view()),
]
