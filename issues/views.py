from django.shortcuts import render
from .models import Bug, Feature, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def all_bugs(request):
    """
    Create a view that will return a list
    of Bugs render them to the 'bugs.html' template
    """
    
    bug_list = Bug.objects.all().order_by('-created_date')

    # Pagination settings
    page = request.GET.get('page', 1)
    paginator = Paginator(bug_list, 2)
    
    try:
        bugs = paginator.page(page)
        
    except PageNotAnInteger:
        
        bugs = paginator.page(1)
        
    except EmptyPage:
        
        bugs = paginator.page(paginator.num_pages)

    return render(request, "bugs.html", {'bugs': bugs})
    
def all_features(request):
    """
    Create a view that will return a list
    of Features render them to the 'features.html' template
    """
    
    feature_list = Feature.objects.all().order_by('-created_date')

    # Pagination settings
    page = request.GET.get('page', 1)
    paginator = Paginator(feature_list, 2)
    
    try:
        features = paginator.page(page)
        
    except PageNotAnInteger:
        
        features = paginator.page(1)
        
    except EmptyPage:
        
        features = paginator.page(paginator.num_pages)

    return render(request, "features.html", {'features': features})