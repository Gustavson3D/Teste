from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CadastroAdminForm, CadastroCidadeForm, CadastroLocalForm, SignUpForm, UpdateuserForm, UpdatePasswordForm
from smarttravel.models import Categorias, Cidade, Local
from django.contrib.admin.views.decorators import staff_member_required


# Paginação
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    cidades = Cidade.objects.all()
    print(request.user)
    return render(request, 'home.html', {'cidades':cidades})

def perfil(request):
        
    return render(request, 'perfil.html')


def cadastro_local(request):
    if request.method == 'GET':
        form = CadastroLocalForm()
        cidades = Cidade.objects.all()
        return render(request, 'cadastro_local.html', {'cidades':cidades, 'form':form})
    elif request.method == 'POST':
        form = CadastroLocalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Local cadastrado com sucesso')
        else:
            return HttpResponse('Erro no formulário. Verifique os dados informados.')
        
    
def local(request, local_id):
    if request.method == 'GET':
        local = get_object_or_404(Local, id=local_id)
        return render(request, "local.html", {'local': local})
    

def cadastro_cidades(request):
    if request.method == 'POST':
        form = CadastroCidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CadastroCidadeForm()

    return render(request, 'cadastro_cidade.html', {'form': form})


def cidade(request, city_slug):
    cidade = get_object_or_404(Cidade, nome_cidade=city_slug)
    categorias = Categorias.objects.all()
    categoria_selecionada = request.GET.get('categoria')
    termo_pesquisa = request.GET.get('q')

    locais = cidade.local.all()

    if categoria_selecionada:
        locais = locais.filter(tipo__categorias=categoria_selecionada)

    if termo_pesquisa:
        locais = locais.filter(nome_local__icontains=termo_pesquisa)

    return render(request, "cidade.html", {'cidade': cidade, 'locais': locais, 'categorias': categorias, 'categoria_selecionada': categoria_selecionada, 'termo_pesquisa': termo_pesquisa})
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logon realizado com sucesso! Bem vindo {username}!')
            return redirect('home')
        else:
            messages.success(request, "Não foi possível autenticar o usuário")
        return redirect('login')
    else:
        return render(request, 'login.html', {})
        

def logout_user(request):
    logout(request)
    messages.success(request, "Deslogado com Sucesso")
    return redirect('home')


def cadastro_usuario(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Seu login como: {username}, foi bem sucedido!')
            return redirect('home')
        else:
            messages.success(request, 'Parece que temos um erro no seu cadastro')
            return redirect('cadastro_usuario')

    return render(request, 'cadastro_usuario.html', {'form':form})


def atualizar_usuario(request):
    if request.user.is_authenticated:
        usuario_atual = User.objects.get(id=request.user.id)
        usuario_form = UpdateuserForm(request.POST or None, instance=usuario_atual)
        if usuario_form.is_valid():
            usuario_form.save()

            login(request, usuario_atual)
            messages.success(request, 'Usuário Atualizado Com Sucesso!')
            return redirect('home')
        return render(request, 'atualizar_usuario.html', {'usuario_form':usuario_form})

    else:
        messages.error(request, 'Faça login para poder modificar sua conta!')
        return redirect(request, 'login.html')


def atualizar_senha(request):
    if request.user.is_authenticated:
        usuario_atual = request.user
        if request.method == 'POST':
            # Asalto
            form = UpdatePasswordForm(usuario_atual, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Senha alterada com sucesso")
                login(request, usuario_atual)
                return redirect('home')
            else: 
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('atualizar_senha')
        else:
            form = UpdatePasswordForm(usuario_atual)
        return render(request, 'atualizar_senha.html', {'form': form})
    
    else:
        messages.success(request, "Você precisa estar logado para mudar sua senha")
        return redirect('home')
    

@staff_member_required # Restrição de acesso apenas para administradores
def cadastro_administrador(request):
    if request.method == 'POST':
        form = CadastroAdminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Definir o usuário como administrador
            user.save()
            messages.success(request, 'Administrador cadastrado com sucesso!')
            return redirect('home')  # Redirecionar para a página inicial após o cadastro
    else:
        form = CadastroAdminForm()
    return render(request, 'cadastro_administrador.html', {'form': form})


    