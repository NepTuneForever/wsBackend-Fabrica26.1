import requests
from django.views import View
from django.views.generic import ListView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Cripto, Favorito

class CryptoListView(View):
    def get(self, request):
        try:
            response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=20", timeout=10)
            if response.status_code == 429:
                return render(request, "criptolist.html", {"criptos": [], "erro": "Muitas requisições, aguarde um instante."})
            elif response.status_code != 200:
                return render(request, "criptolist.html", {"criptos": [], "erro": f"Erro na API encontrado: {response.status_code}"})

            for c in response.json():
                Cripto.objects.update_or_create(simbolo=c['symbol'], defaults={ 'nome': c['name'], 'preco': c['current_price'] })

            favoritos = list(Favorito.objects.values_list('simbolo', flat=True)) # Tava vindo como tupla dentro de listas, converti pra apenas lista (usando flat=True)
            criptos = []
            for c in response.json():
                if c['symbol'] not in favoritos:
                    criptos.append(c)

        except Exception as e:
            return render(request, "criptolist.html", {"criptos": [], "erro": str(e)})

        return render(request, "criptolist.html", {"criptos": criptos, "erro": None})

    def post(self, request):
        Favorito.objects.create( nome = request.POST.get('cripto_name'), simbolo = request.POST.get('cripto_symbol'), preco  = request.POST.get('cripto_price'))
        return redirect('cripto-list')

class VerFavoritos(ListView):
    model = Favorito
    template_name = 'favoritos.html'
    context_object_name = 'cripto_favoritos'

    def post(self, request):
        favorito_id = request.POST.get('favorito_id')
        Favorito.objects.filter(id=favorito_id).delete()
        return redirect('ver-favoritos')
    
class AnalisarPrecos(ListView):
    model = Favorito
    template_name = 'analisarprecos.html'
    context_object_name = 'favoritos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mais_caro']   = Favorito.objects.order_by('-preco').first()
        context['mais_barato'] = Favorito.objects.order_by('preco').first()
        context['total']       = sum(f.preco for f in context['favoritos'])

        return context
    
class AtualizarPrecos(UpdateView):
    model = Favorito
    fields = ['preco']
    template_name = 'atualizarprecos.html'
    success_url = reverse_lazy('analisar-precos')


# Source - https://stackoverflow.com/a/41085356
# Posted by Ibrahim Kasim, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-21, License - CC BY-SA 4.0

# >>> list(Article.objects.values_list('id', flat=True)) # flat=True will remove the tuples and return the list   
# [1, 2, 3, 4, 5, 6]

# >>> list(Article.objects.values('id'))
# [{'id':1}, {'id':2}, {'id':3}, {'id':4}, {'id':5}, {'id':6}]
