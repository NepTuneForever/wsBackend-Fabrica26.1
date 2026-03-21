from django.urls import path
from .views import CryptoListView, VerFavoritos
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', CryptoListView.as_view(), name='cripto-list'),
    path('favoritos/', VerFavoritos.as_view(), name='ver-favoritos'),
    path('login/', obtain_auth_token),
]

# Superuser criado para acessar a API de autenticação do Django rest framework;
# so colocar user e senha que por padrao, o django rest ja pega "username" e "password";
# e retorna o token de autenticação;

# Usei o postman pra testar a API

# POST: http://127.0.0.1:8000/api/login/

# JSON:
# {
#     "username": "neptune",
#     "password": "kali"
# }

# Response:
# {
#     "token": "622b94d816861ed7f980043418bcf4d67b3c1202"
# }