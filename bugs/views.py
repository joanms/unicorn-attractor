from django.shortcuts import render

# Create your views here.
def report_bug(request):
    return render(request, "report_bug.html") 