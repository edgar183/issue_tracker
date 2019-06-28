from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
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
        form = BugForm(request.POST or None, instance=bug)
        if form.is_valid():
            form.instance.author = request.user
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, "bugform.html", {'form': form})


@login_required()
def create_or_edit_bug_comment(request, bug_pk, pk=None):
    bug = get_object_or_404(Bug, pk=bug_pk)
    comment = get_object_or_404(CommentBug, pk=pk) if pk else None
    if request.method == "POST":
        form = CommentBugForm(request.POST, instance=comment)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.bug = bug
            form.save()
            messages.success(request, 'New Comment Added!')
            return redirect(bug_detail, bug_pk)
    else:
        form = CommentBugForm(instance=comment)
    return render(request, 'bugcommentform.html', {'form': form})


@login_required()
def upvote_bug(request, pk):
    bug = Bug.objects.get(pk=pk)
    bug.upvotes += 1
    bug.save()
    messages.success(request, 'Bug upvoted!')
    return redirect('bug_detail', pk)

@login_required()
def delete_bug(request, pk=None):
    bug_id = int(pk)
    obj = get_object_or_404(Bug, pk=bug_id)
    if obj.author == request.user or request.user.is_staff: 
        if request.method == 'POST':
            bug_id = int(pk)
            obj = get_object_or_404(Bug, pk=bug_id)
            obj.delete()

            return redirect('bugs')
    else:
         messages.success(request, 'You do not have premission to delete this bug.')

def delete_bug_comment(request, bug_pk, pk=None):
    bug = get_object_or_404(Bug, pk=bug_pk)
    comment_id = int(pk)
    obj = get_object_or_404(CommentBug, pk=comment_id)
    if request.user == obj.author or request.user.is_staff:   
        if request.method == 'POST':
            obj.delete()
            messages.success(request, 'The comment has been deleted.')
            return redirect('bug_detail', bug_pk)
    else:
         messages.success(request, 'You do not have premission to delete this comment.')

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
    comments = CommentFeature.objects.filter(feature=pk)
    return render(request, "featuredetail.html", {'feature': feature, 'comments': comments})


@login_required()
def create_or_edit_feature(request, pk=None):
    """
     Create a view that allows us to create
    or edit a feature depending if the Feature ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST or None, instance=feature)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.price = 10
            feature = form.save()
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, "featureform.html", {'form': form})


@login_required()
def create_or_edit_feature_comment(request, feature_pk, pk=None):
    feature = get_object_or_404(Feature, pk=feature_pk)
    comment = get_object_or_404(CommentFeature, pk=pk) if pk else None
    if request.method == "POST":
        form = CommentFeatureForm(request.POST, instance=comment)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.feature = feature
            form.save()
            messages.success(request, 'New Comment Added!')
            return redirect(feature_detail, feature_pk)
    else:
        form = CommentFeatureForm(instance=comment)
    return render(request, 'featurecommentform.html', {'form': form})


@login_required()
def upvote_feature(request, pk):
    feature = Feature.objects.get(pk=pk)
    feature.upvotes += 1
    feature.save()
    messages.success(request, 'Feature upvoted!')
    return redirect('feature_detail', pk)

@login_required()
def delete_feature(request, pk=None):
    if request.method == 'POST':
        feature_id = int(pk)
        obj = get_object_or_404(Feature, pk=feature_id)
        obj.delete()

        return redirect('features')
