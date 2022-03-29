from django.db import models
from django.forms import ModelForm
from django import forms
import uuid

class Flan(models.Model):
  flaun_uuid = models.UUIDField()
  name = models.CharField(max_length=64)
  description = models.TextField()
  image_url = models.URLField()
  slug =  models.SlugField()
  is_private = models.BooleanField()
  
  
class ContactForm(models.Model):
  contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  customer_email = models.EmailField()
  customer_name = models.CharField(max_length=64)
  message = models.TextField(default='uuid.uuid4')
  

class SearchForm(models.Model):
  query = models.CharField(max_length=64)
  
  
class ContactFormForm(forms.Form):
  customer_email = forms.EmailField(label='Correo')
  customer_name = forms.CharField(max_length=64, label='Nombre')
  message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'name':'body', 'rows':'10', 'cols':'40'}))


class ContactFormModelForm(ModelForm):
  class Meta:
    model = ContactForm
    fields = ['customer_email','customer_name','message']

class SearchFormModelForm(ModelForm):
  class Meta:
    model = SearchForm
    fields = ['query']



  