# 📈 Cripto API

API REST para consulta e gerenciamento de criptomoedas, com suporte a favoritos e integração com API externa de cotações em tempo real.

Desenvolvido com **Django**, **Django REST Framework** e conteinerizado com **Docker**.

---

## 📋 Índice

- [Tecnologias](#-tecnologias)
- [Requisitos](#-requisitos)
- [Instalação e execução](#-instalação-e-execução)
- [Variáveis de ambiente](#-variáveis-de-ambiente)
- [Endpoints da API](#-endpoints-da-api)
- [Modelos](#-modelos)
- [Estrutura do projeto](#-estrutura-do-projeto)

---

## 🛠 Tecnologias

- [Python 3.12](https://www.python.org/)
- [Django 6.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL 16](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ✅ Requisitos

Antes de começar, você precisa ter instalado na sua máquina:

- [Docker Desktop](https://www.docker.com/products/docker-desktop) — inclui o Docker e o Docker Compose

> Não é necessário instalar Python, PostgreSQL ou qualquer dependência manualmente. O Docker cuida de tudo.

---

## 🚀 Instalação e execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```

### 2. Crie o arquivo de variáveis de ambiente

Na raiz do projeto, crie um arquivo `.env` com o seguinte conteúdo:

```env
SECRET_KEY=django-insecure-troque-pela-sua-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=cripto_db
DB_USER=postgres
DB_PASSWORD=senha123
DB_HOST=db
DB_PORT=5432
```

> ⚠️ O arquivo `.env` nunca deve ser enviado ao GitHub. Ele já está listado no `.gitignore`.

### 3. Suba os containers

```bash
docker compose up --build
```

> Na primeira execução, use `--build`. Nas próximas, pode usar apenas `docker compose up`.

### 4. Execute as migrations

Em outro terminal, com os containers já rodando:

```bash
docker compose exec web python manage.py migrate
```

### 5. (Opcional) Crie um superusuário

```bash
docker compose exec web python manage.py createsuperuser
```

### 6. Acesse a aplicação

| Recurso | URL |
|---|---|
| API | http://localhost:8000/api/ |
| Admin | http://localhost:8000/admin/ |

---

## ⚙️ Variáveis de ambiente

| Variável | Descrição | Exemplo |
|---|---|---|
| `SECRET_KEY` | Chave secreta do Django | `django-insecure-...` |
| `DEBUG` | Modo de depuração | `True` ou `False` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |
| `DB_NAME` | Nome do banco de dados | `cripto_db` |
| `DB_USER` | Usuário do PostgreSQL | `postgres` |
| `DB_PASSWORD` | Senha do PostgreSQL | `senha123` |
| `DB_HOST` | Host do banco (nome do serviço no Docker) | `db` |
| `DB_PORT` | Porta do PostgreSQL | `5432` |

---

## 📡 Endpoints da API

### Criptomoedas

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/criptos/` | Lista todas as criptomoedas |
| `POST` | `/api/criptos/` | Cadastra uma nova criptomoeda |
| `GET` | `/api/criptos/{id}/` | Retorna uma criptomoeda pelo ID |
| `PUT` | `/api/criptos/{id}/` | Atualiza uma criptomoeda |
| `DELETE` | `/api/criptos/{id}/` | Remove uma criptomoeda |

### Favoritos

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/favoritos/` | Lista todos os favoritos |
| `POST` | `/api/favoritos/` | Adiciona uma criptomoeda aos favoritos |
| `GET` | `/api/favoritos/{id}/` | Retorna um favorito pelo ID |
| `PUT` | `/api/favoritos/{id}/` | Atualiza um favorito |
| `DELETE` | `/api/favoritos/{id}/` | Remove um favorito |

### API Externa

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/cotacao/` | Consulta cotações em tempo real via API externa |

---

## 🗄 Modelos

### Cripto

Representa uma criptomoeda cadastrada no sistema.

| Campo | Tipo | Descrição |
|---|---|---|
| `nome` | CharField | Nome da criptomoeda |
| `simbolo` | CharField | Símbolo (ex: BTC, ETH) |
| `preco` | FloatField | Preço atual |

### Favorito

Representa uma criptomoeda marcada como favorita pelo usuário.

| Campo | Tipo | Descrição |
|---|---|---|
| `cripto` | ForeignKey | Referência à criptomoeda (Cripto) |
| `nome` | CharField | Nome da criptomoeda |
| `simbolo` | CharField | Símbolo da criptomoeda |
| `preco` | FloatField | Preço no momento em que foi favoritada |

---

## 📁 Estrutura do projeto

```
wsBackend-Fabrica26.1/
├── core/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── cripto/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env               # variáveis de ambiente (não versionar)
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🐳 Comandos Docker úteis

```bash
# Subir os containers
docker compose up

# Subir em background
docker compose up -d

# Parar os containers
docker compose down

# Ver logs
docker compose logs web

# Acessar o terminal do container
docker compose exec web bash

# Rodar comandos Django
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

---

## 👥 Autores

Desenvolvido para o processo seletivo da **Fábrica de Software — Turma 26.1**.
