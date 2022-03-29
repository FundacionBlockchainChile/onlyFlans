from django.contrib import admin
from .models import Flan, ContactForm, SearchForm

# Register your models here.
admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(SearchForm)