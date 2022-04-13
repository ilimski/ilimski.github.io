from django.shortcuts import render
from django.views.generic import ListView
from core.models import Faculty


class CoreView(ListView):
    template_name = 'index.html'
    queryset = Faculty.objects.all()
    context_object_name = 'facs'