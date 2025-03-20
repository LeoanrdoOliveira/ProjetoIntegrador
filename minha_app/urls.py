from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listagem/', views.listagem, name='listagem'),
    path('receitas/', views.receitas, name='receitas'),
]