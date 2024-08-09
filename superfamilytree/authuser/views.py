from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from superhero.models import SuperHero
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authuser/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
            # Gestion d'un mail ou mot de passe incorrect
                return render(request, 'authuser/login.html', {'error': 'Invalid email or password'})
    else:
        form = LoginForm()
    return render(request, 'authuser/login.html', {'form': form})
    
def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'authuser/home.html', context)

def home(request):
    heroes = SuperHero.objects.all()
    paginator = Paginator(heroes, 7)

    page = request.GET.get('page')

    try:
        heroes = paginator.page(page)
    except PageNotAnInteger:
        heroes = paginator.page(1)
    except EmptyPage:
        heroes = paginator.page(paginator.num_pages)


    return render(request, 'authuser/home.html', {'heroes': heroes})