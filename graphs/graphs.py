import pygal
from bugs.models import Bug
from features.models import Feature
from pygal.style import Style


custom_style = Style(
    background = 'transparent',
    plot_background = 'transparent',
    font_family = 'Roboto',
    legend_font_size = 25,
    value_font_size=25, 
    label_font_size=25,
    major_label_font_size=25)


def bug_pie_chart():
    
    """A pie chart showing the status of bugs"""

    todo = Bug.objects.filter(status='To do').count()
    inprogress = Bug.objects.filter(status='In progress').count()
    done = Bug.objects.filter(status='Done').count()
    cancelled = Bug.objects.filter(status='Cancelled').count()
    p_chart = pygal.Pie(
        print_values=True, 
        style=custom_style
    )

    p_chart.add('To Do', todo)
    p_chart.add('In Progress', inprogress)
    p_chart.add('Done', done)
    p_chart.add('Cancelled', cancelled)
    return p_chart.render()

def BugPieChart():
    
    """Enable importing the graph into a view"""
    
    chart = bug_pie_chart()
    return chart

    
def feature_pie_chart():
    
    """A pie chart showing the status of features"""

    todo = Feature.objects.filter(status='To do').count()
    inprogress = Feature.objects.filter(status='In progress').count()
    done = Feature.objects.filter(status='Done').count()
    cancelled = Feature.objects.filter(status='Cancelled').count()
    p_chart = pygal.Pie(
        print_values=True,
        style=custom_style
    )

    p_chart.add('To Do', todo)
    p_chart.add('In Progress', inprogress)
    p_chart.add('Done', done)
    p_chart.add('Cancelled', cancelled)
    return p_chart.render()

def FeaturePieChart():
    
    """Enable importing the graph into a view"""
    
    chart = feature_pie_chart()
    return chart    
    
    
def bug_bar_chart():
    
    """A bar chart showing the 5 most upvoted bugs in descending order"""

    bugs = Bug.objects.order_by('-upvotes')[:5]
    bar_chart = pygal.Bar(
        show_minor_y_labels=False,
        print_values=True,
        print_zeroes=False,
        style=custom_style
    )

    for bug in bugs:
        bar_chart.add(bug.title, bug.upvotes)

    return bar_chart.render()

def BugBarChart():
    
    """Enable importing the graph into a view"""
    
    chart = bug_bar_chart()
    return chart


def feature_bar_chart():
    
    """A bar chart showing the 5 highest-paid features in descending order"""

    features = Feature.objects.order_by('-amount_paid')[:5]
    bar_chart = pygal.Bar(
        print_values=True,
        print_zeroes=False,
        style=custom_style
    )

    for feature in features:
        bar_chart.add(feature.title, feature.amount_paid)

    return bar_chart.render()

def FeatureBarChart():
    
    """Enable importing the graph into a view"""
    
    chart = feature_bar_chart()
    return chart