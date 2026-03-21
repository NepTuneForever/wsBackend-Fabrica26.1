import requests
from django.views import View
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect, render
from .models import Cripto, User
from django.urls import reverse_lazy

class CryptoListView(View):
    def get(self, request):
        try:
            response = requests.get(
                "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
            )
            criptos = response.json()
        except:
            criptos = []

        return render(request, "criptolist.html", {"criptos": criptos})
    
    # JSON CRIPTO: 
    # name;
    # symbol;
    # current_price;

class FavoritarView(CreateView):
    model = User
    fields = '__all__'
    template_name = 'favoritar.html'
    success_url = reverse_lazy('cripto-list')