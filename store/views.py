from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from store.models import Clothes

class HomePage(ListView):
    model = Clothes
    template_name = "store/index.html"
    context_object_name = "clothes"


class DetailPage(DetailView):
    model = Clothes
    template_name = "store/detail.html"
    context_object_name = "clothes"
