from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperHero
from .forms import SuperHeroForm

# gérer l'affichage d'un enfant sans duplication (récursivité)
def get_unique_children(hero, seen=None):
    if seen is None:
       seen = set()
    unique_children = []
    for child in hero.children.all():
        if child not in seen:
            seen.add(child)
            unique_children.append(child)
            unique_children.extend(get_unique_children(child, seen))
    return unique_children

# View du superhéros, de ses enfants, modification et suppression
def superhero_detail(request, pk): 
    hero = get_object_or_404(SuperHero, pk=pk)

    if request.method == 'POST':
        if 'modify' in request.POST:
            form = SuperHeroForm(request.POST, instance=hero)
            if form.is_valid():
                form.save()
                return redirect('superhero_detail', pk=pk)
        elif 'delete' in request.POST:
            hero.delete()
            return redirect('home')
    else:
        form = SuperHeroForm(instance=hero)

    unique_children = get_unique_children(hero)

    context = {
        'hero': hero,
        'form': form,
        'parents': hero.parent,
        'children': unique_children,
        'seen': set(),
    }
    return render(request, 'superhero/superhero_detail.html', context)

# Ajout d'un superhéros
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
def search_hero(request):
    query = request.GET.get('q')
    if query:
        heroes = SuperHero.objects.filter(name__icontains=query)
        if heroes.count() == 1:
            return redirect('superhero_detail', pk=heroes.first().pk)
    else:
        heroes = SuperHero.objects.all()

    return render(request, 'authuser/home.html', {'heroes': heroes, 'query': query})