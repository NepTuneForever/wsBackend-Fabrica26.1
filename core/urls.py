from django.urls import path
from .views import CryptoListView, VerFavoritos

urlpatterns = [
    path('', CryptoListView.as_view(), name='cripto-list'),
    path('favoritos/', VerFavoritos.as_view(), name='ver-favoritos'),
]