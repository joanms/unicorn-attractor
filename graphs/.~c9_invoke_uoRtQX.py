from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, View

# The code in this file is based on this video: https://bit.ly/2K5VDCX

class GraphsAjaxView(View):
    
    """Displays the graphs page"""
    
    template_name = "graphs.html"
    
    def get(self, request, *args, **kwargs):
        data = {}
        data['labels'] = ["To Do", "In Progress", "Done", "Can"]
        return JsonResponse(data)