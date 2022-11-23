from django.shortcuts import render
from django.views.generic import TemplateView


class HelloView(TemplateView):
    template_name = 'index.html'
