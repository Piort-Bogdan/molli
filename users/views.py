from django.shortcuts import render
from django.views import generic

from .models import User, Pet

class registration(generic.CreateView):
    model = User
    queryset = User.objects.all()

