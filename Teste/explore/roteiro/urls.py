from django.urls import path
from . import views


urlpatterns = [
    # sumario inicial do carrinho de compras/roteiro
    path('', views.sumario, name='sumario'),
    path("adicionar/", views.adicionar_elementos, name="adicionar_elementos"),
    path('deletar/', views.deletar_elementos, name='deletar_elementos'),
    path("atualizar/", views.atualizar_elementos, name="atualizar_elementos"),
]