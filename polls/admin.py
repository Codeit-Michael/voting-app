from django.contrib import admin
from .models import question,choice

# Register your models here.
admin.site.register(question)
admin.site.register(choice)