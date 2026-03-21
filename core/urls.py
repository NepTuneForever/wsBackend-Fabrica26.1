from django.urls import path
from .views import CryptoListView, FavoritarView

urlpatterns = [
    path('', CryptoListView.as_view(), name='cripto-list'),
    path('favoritar/', FavoritarView.as_view(), name='favoritar'),
]