import requests
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Cripto, Favorito

class CryptoListView(View):
    def get(self, request):
        try:
            response = requests.get(
                "https://api.coingecko.com/api/v3/coins/markets",
                params={
                    "vs_currency": "usd",
                    "per_page": 20,
                    "page": 1,
                },
                timeout=10
            )
            if response.status_code == 429:
                criptos = []
                erro = "Muitas requisições. Aguarde alguns segundos e recarregue."
            elif response.status_code != 200:
                criptos = []
                erro = f"Erro na API: {response.status_code}"
            else:
                criptos = response.json()
                erro = None
        except Exception as e:
            criptos = []
            erro = str(e)

        return render(request, "criptolist.html", {"criptos": criptos, "erro": erro})

    def post(self, request):
        Favorito.objects.create(
            nome    = request.POST.get('cripto_name'),
            simbolo = request.POST.get('cripto_symbol'),
            preco   = request.POST.get('cripto_price'),
        )
        return redirect('cripto-list')

class VerFavoritos(ListView):
    model = Favorito
    template_name = 'favoritos.html'
    context_object_name = 'cripto_favoritos'
    success_url = reverse_lazy('ver-favoritos')

