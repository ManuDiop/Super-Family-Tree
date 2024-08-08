from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperHero
from .forms import SuperHeroForm

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

    context = {
        'hero': hero,
        'form': form,
        'parents': hero.parent,
        'children': hero.children.all()
    }
    return render(request, 'superhero/superhero_detail.html', context)

