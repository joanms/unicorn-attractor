from django.shortcuts import render
from django.http import JsonResponse

def graphs(request):
    """A view that displays the graphs page"""
    return render(request, "graphs.html")