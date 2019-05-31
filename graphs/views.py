from django.shortcuts import render
from .graphs import BugPieChart, FeaturePieChart, BugBarChart, FeatureBarChart

def graphs(request):
    """A view that displays the graphs page"""
    return render(request, "graphs.html", {'bug_pie_chart': BugPieChart, 'feature_pie_chart': FeaturePieChart, 'bug_bar_chart': BugBarChart, 'feature_bar_chart': FeatureBarChart})