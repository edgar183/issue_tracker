from django.shortcuts import render, get_object_or_404
from itertools import chain
from django.db.models import Q
from issues.models import Bug, Feature


def search(request):
    bugs = Bug.objects.filter(
        Q(title__contains=request.GET['q']) | Q(tag__contains=request.GET['q']))
    feature = Feature.objects.filter(
        Q(title__contains=request.GET['q']) | Q(tag__contains=request.GET['q']))
    results = chain(bugs, feature)
    #bug = get_object_or_404(Bug, pk=pk)
    #feature = get_object_or_404(Feature, pk=pk)
    context = {
        "results": results,
        #"bug": bug,
        #"feature": feature,
    }
    return render(request, "results.html", context)
