from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView

class GraphView(TemplateView):
    template_name = "graphs.html"
