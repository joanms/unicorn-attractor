import pygal
from bugs.models import Bug
from features.models import Feature
from pygal.style import Style

def bug_pie_chart():
    """Show summary for features"""

    todo = Bug.objects.filter(status='To do').count()
    inprogress = Bug.objects.filter(status='In progress').count()
    done = Bug.objects.filter(status='Done').count()
    cancelled = Bug.objects.filter(status='Cancelled').count()
    p_chart = pygal.Pie(
        print_values=True,
    )

    p_chart.add('To Do', todo)
    p_chart.add('In Progress', inprogress)
    p_chart.add('Done', done)
    p_chart.add('Cancelled', cancelled)
    return p_chart.render()

def BugPieChart():
    chart = bug_pie_chart()
    return chart
    
def feature_pie_chart():
    """Show summary for features"""

    todo = Feature.objects.filter(status='To do').count()
    inprogress = Feature.objects.filter(status='In progress').count()
    done = Feature.objects.filter(status='Done').count()
    cancelled = Feature.objects.filter(status='Cancelled').count()
    p_chart = pygal.Pie(
        print_values=True,
    )

    p_chart.add('To Do', todo)
    p_chart.add('In Progress', inprogress)
    p_chart.add('Done', done)
    p_chart.add('Cancelled', cancelled)
    return p_chart.render()

def FeaturePieChart():
    chart = feature_pie_chart()
    return chart    