from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from bugs.models import Bug
from features.models import Feature
import json


def graphs(request):
    """A View that renders the graph page"""
    return render(request, "graphs.html")


def get_data(request):
    """
    A view that fetches the data for the graphs. 
    This was adapted from Anthony Bonello's project: 
    https://github.com/abonello/project_5/blob/master/issuetracker/views.py
    """
    Bugs = Bug.objects.all()
    Features = Feature.objects.all()

    bug_count = 0
    feature_count = 0

    bugs = []
    features = []

    for each in Bugs:
        bug_count += 1
        item = {}
        item['title'] = each.title
        item['upvotes'] = each.upvotes
        item['status'] = each.status
        bugs.append(item)

    for each in Features:
        feature_count += 1
        item = {}
        item['title'] = each.title
        item['upvotes'] = each.upvotes
        item['status'] = each.status
        features.append(item)

    data = {}
    data['features'] = features
    data['bugs'] = bugs
    response_data = {}
    try:
        response_data['result'] = 'Success'
        response_data['message'] = data
    except:
        response_data['result'] = 'Error'
        response_data['message'] = 'Something went wrong'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
