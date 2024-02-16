from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CadastroCidadeForm, CadastroLocalForm, SignUpForm
from smarttravel.models import Categorias, Cidade, Local


def home(request):
    cidades = Cidade.objects.all()
    print(request.user)
    return render(request, 'home.html', {'cidades':cidades})


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
    if request.method == 'GET':
        cidade = Cidade.objects.get(nome_cidade=city_slug)
        categorias = Categorias.objects.all()
        categoria = request.GET.get('categoria')
        if categoria is None:
            local = cidade.local.all()
        else:
            local = Local.objects.filter(cidade__nome_cidade=city_slug, tipo__categorias=categoria)
        return render(request, "cidade.html", {'cidade':cidade, 'locais':local, 'categorias':categorias})
    

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