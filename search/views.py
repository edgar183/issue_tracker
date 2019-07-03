from django.shortcuts import render
from itertools import chain
from django.db.models import Q
from issues.models import Bug, Feature


def search(request):
    bugs = Bug.objects.filter(Q(title__contains=request.GET['q']) | Q(tag__contains=request.GET['q']))
    feature = Feature.objects.filter(Q(title__contains=request.GET['q']) | Q(tag__contains=request.GET['q']))
    results = chain(bugs, feature)
    return render(request, "results.html", {"results": results})
