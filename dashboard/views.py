from django.shortcuts import render
from datetime import datetime, timedelta, time
from django.db.models import Count
from issues.models import Bug, Feature
from django.http import JsonResponse
import json

# Create your views here.


def chart(request):
    count_bugs = Bug.objects.all().count()
    count_features = Feature.objects.all().count()
    context = {
        'bugs': count_bugs,
        'features': count_features
    }
    return render(request, "dashboard.html", context)

def get_bug_status_json(request):
    lables = ["Todo", "Doing", "Done"]
    count_todo = Bug.objects.filter(status='TODO').count()
    count_doing = Bug.objects.filter(status="DOING").count()
    count_done = Bug.objects.filter(status="DONE").count()
    data = {
        'lables': lables,
        'count': [count_todo, count_doing, count_done],
    }
    return JsonResponse(data)


def get_feature_status_json(request):
    lables = ["Todo", "Doing", "Done"]
    count_todo = Feature.objects.filter(status='TODO').count()
    count_doing = Feature.objects.filter(status="DOING").count()
    count_done = Feature.objects.filter(status="DONE").count()
    data = {
        'lables': lables,
        'count': [count_todo, count_doing, count_done],

    }

    return JsonResponse(data)


def get_bug_upvotes_json(request):
    bug_titles = []
    bug_upvotes = []
    dataset = list(Bug.objects.values('upvotes', 'title').exclude(
        upvotes=0).order_by('upvotes'))
    for item in dataset:
        bug_titles.append(item['title'])
        bug_upvotes.append(item['upvotes'])

    data = {
        'lables': bug_titles,
        'dataset': bug_upvotes
    }
    return JsonResponse(data)


def get_feature_upvotes_json(request):
    feature_titles = []
    feature_upvotes = []
    dataset = list(Feature.objects.values('upvotes', 'title').exclude(
        upvotes=0).order_by('upvotes'))
    for i in dataset:
        feature_titles.append(i['title'])
        feature_upvotes.append(i['upvotes'])
    data = {
        'lables': feature_titles,
        'dataset': feature_upvotes
    }
    return JsonResponse(data)
