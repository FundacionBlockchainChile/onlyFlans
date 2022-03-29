import re
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flan, ContactForm, ContactFormForm, ContactFormModelForm, SearchFormModelForm
from django.contrib.auth.decorators import login_required
import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.


def inicio(request):
  flans = Flan.objects.all()
  private_flans = Flan.objects.filter(is_private=True)
  context = {
    'flans': flans,
    'private_flans': private_flans}
  return render(request, 'index.html', context)


def about(request):
  return render(request, 'about.html') 


@login_required
def welcome(request):
  private_flans = Flan.objects.filter(is_private=True)
  context = {
    'private_flans': private_flans}
  return render(request, 'welcome.html', context) 


def contacto(request):
  if request.method == 'POST':
    form = ContactFormModelForm(request.POST)
    if form.is_valid():
      contact_form = ContactForm.objects.create(**form.cleaned_data)
      return HttpResponseRedirect('/success/')
  else:
    form = ContactFormForm()
  return render(request, 'contactus.html', {'form': form}) 

def success(request):
  return render(request, 'success.html', {})


def recipe(request, id):
    print(id)
    context = {
        'card_url': '',
      }  
    try:
      API_KEY = os.getenv('API_KEY')
      url = os.getenv('URL')
      url = f'https://api.spoonacular.com/recipes/{id}/card?&apiKey={API_KEY}'
      card_url = requests.get(url).json()
      print(card_url)
      context = {
        'card_url': card_url,
      }  
      return render(request, 'recipe.html', context)
    except:
      return render(request, 'recipe.html', context)
  

def recipes(request):
  form = SearchFormModelForm()
  context = {
        'form': form,
        'recipes': []
      }  
  if request.method == 'POST':
    try:
      name = request.POST['query']
      API_KEY = os.getenv('API_KEY')
      url = os.getenv('URL')
      url = f'{url}/recipes/complexSearch?query={name}&apiKey={API_KEY}'
      recipes = requests.get(url).json()['results']
      context = {
        'form': form,
        'recipes': recipes
      }  
      return render(request, 'recipes.html',context)
    except:
      return render(request, 'recipes.html',context)
  else:
    return render(request, 'recipes.html',context)




