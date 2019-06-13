from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Bug, Feature, CommentBug, CommentFeature
from .forms import BugForm, FeatureForm, CommentBugForm, CommentFeatureForm



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
    
@login_required()    
def bug_form(request):
    """
    Add new bug in system.
    """
    form = BugForm(request.POST or None)
    # if request.method == "POST":
    #         #     if form.is_valid():
    #         form.instance.author = request.user
    #         if form.instance.issue_type == 'FEATURE':
    #             form.instance.price = 100
    #         else:
    #             form.instance.price = 0
    #         #bug = form.save()
            
    #         return redirect(all_bugs)
    # else:
    #     form = BugForm()
    return render(request, "bugform.html", {'form': form})


# @login_required()
# def edit_issue(request, pk=None):
#     """
#     Create a view that allows us to edit a issue depending if the Issue ID
#     is null or not
#     """
#     issue = get_object_or_404(Issue, pk=pk) if pk else None
#     user = request.user
#     # Prevents a non-staff user from editing another users comment
#     if not request.user.is_staff:
#         if user.id != request.user.id:
#             messages.success(
#                 request,
#                 'You Do Not Have Permission To Edit this Issue'
#             )
#             return redirect(issue_detail, issue.pk)

#     if request.method == "POST":
#         form = IssueForm(request.POST, request.FILES, instance=issue)
#         if form.is_valid():

#             form.instance.author = request.user
#             if form.instance.issue_type == 'FEATURE':
#                 form.instance.price = 100
#             else:
#                 form.instance.price = 0
#             issue = form.save()
#             notify.send(request.user, recipient=issue.author, verb="updated your Issue: " + issue.title)
#             messages.success(request, 'Issue Edited with success!')

#             return redirect(issue_detail, issue.pk)
#     else:
#         form = IssueForm(instance=issue)
#     return render(request, 'issueform.html', {'form': form})