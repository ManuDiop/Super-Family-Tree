from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperHero
from .forms import SuperHeroForm
from django.contrib.auth.decorators import login_required

# View du superhéros, de ses enfants, modification et suppression
@login_required
def superhero_detail(request, pk): 
    hero = get_object_or_404(SuperHero, pk=pk)

    if request.method == 'POST':
        if 'modify' in request.POST:
            form = SuperHeroForm(request.POST, instance=hero)
            if form.is_valid():
                form.save()
                return redirect('home')
        elif 'delete' in request.POST:
            hero.delete()
            return redirect('home')
    else:
        form = SuperHeroForm(instance=hero)

    parents = []
    current_hero = hero.parent
    while current_hero:
        parents.append(current_hero)
        current_hero = current_hero.parent

    def get_descendants(hero):
        descendants = []
        for child in hero.children.all():
            descendants.append(child)
            descendants.extend(get_descendants(child))
        return descendants
    
    descendants = get_descendants(hero)

    context = {
        'hero': hero,
        'form': form,
        'parents': parents[::-1],
        'children': hero.children.all(),
        'descendants': descendants
    }
    return render(request, 'superhero/superhero_detail.html', context)

# Ajout d'un superhéros
@login_required
def add_superhero(request):
    if request.method == 'POST':
        form = SuperHeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SuperHeroForm()

    return render(request, 'superhero/add_superhero.html', {'form': form})

# Résultat de la recherche
login_required
def search_hero(request):
    query = request.GET.get('q')
    if query:
        heroes = SuperHero.objects.filter(name__icontains=query)
        if heroes.count() == 1:
            return redirect('superhero_detail', pk=heroes.first().pk)
        elif heroes.count() == 0:
            return render(request, '404.html', status=404)
    else:
        heroes = SuperHero.objects.all()

    return render(request, 'authuser/home.html', {'heroes': heroes, 'query': query})

