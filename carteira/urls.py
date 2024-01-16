from django.urls import path

from .views import carteira, adicionar_transacao


urlpatterns = [
    path('', carteira, name='carteira'),
    path('adicionar/', adicionar_transacao, name='adicionar_transacao'),
]
