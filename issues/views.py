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

def bug_detail(request, pk):
    """
    Create a view that returns a single
    Bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the bug is
    not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    comments = CommentBug.objects.filter(bug=pk)
    return render(request, "bugdetail.html", {'bug': bug, 'comments': comments})


@login_required()
def create_or_edit_bug(request, pk=None):
    """
     Create a view that allows us to create
    or edit a bug depending if the Bug ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        bug_form = BugForm(request.POST or None, instance=bug)
        if bug_form.is_valid():
            bug_form.instance.author = request.user
            bug = bug_form.save()
            return redirect(bug_detail, bug.pk)
    else:
        bug_form = BugForm(instance=bug)
    return render(request, "bugform.html", {'form': bug_form})

@login_required()
def create_or_edit_bug_comment(request, pk=None):
    return render(request, "bugform.html")

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
    
def feature_detail(request, pk):
    """
    Create a view that returns a single
    Feature object based on the feature ID (pk) and
    render it to the 'featuredetail.html' template.
    Or return a 404 error if the feature is
    not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    return render(request, "featuredetail.html", {'feature': feature})


@login_required()
def create_or_edit_feature(request, pk=None):
    """
     Create a view that allows us to create
    or edit a feature depending if the Feature ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        feature_form = FeatureForm(request.POST or None, instance=feature)
        if feature_form.is_valid():
            feature_form.instance.author = request.user
            feature_form.instance.price = 10
            feature = feature_form.save()
            return redirect(feature_detail, feature.pk)
    else:
        feature_form = FeatureForm(instance=feature)
    return render(request, "featureform.html", {'form': feature_form})

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
