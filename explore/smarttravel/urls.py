from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cidade/<int:cidade_id>/', views.cidade, name='cidade'),
    path('local/<int:local_id>/', views.local, name='local'),
    path('cadastro_local/', views.cadastro_local, name='cadastro_local'),
    path('cadastro_cidade/', views.cadastro_cidades, name='cadastro_cidade'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('atualizar_usuario/', views.atualizar_usuario, name='atualizar_usuario'),
    path('atualizar_senha/', views.atualizar_senha, name='atualizar_senha'),
    path('cadastro_administrador/', views.cadastro_administrador, name='cadastro_administrador'),
    path('perfil/', views.perfil, name='perfil'),
]