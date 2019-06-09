from django.shortcuts import render

def graphs(request):
    """A view that displays the graphs page"""
    return render(request, "graphs.html")