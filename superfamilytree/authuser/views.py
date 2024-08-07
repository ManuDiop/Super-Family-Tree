from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authuser/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Gestion d'un mail ou mot de passe incorrect
            return render(request, 'authuser/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'authuser/login.html')
    
def logout(request):
    logout(request)
    return redirect('home')