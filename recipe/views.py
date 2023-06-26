from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe
from django.contrib import messages

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_recipes')
    else:
        form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form': form})

def list_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/list_recipes.html', {'recipes': recipes})



def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('list_recipes')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe/update_recipe.html', {'form': form})

def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe deleted successfully.')
    return redirect('list_recipes')

def search_recipes(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(name__icontains=query)
    return render(request, 'recipe/search_recipes.html', {'recipes': recipes, 'query': query})
