from django.shortcuts import render
from datetime import datetime, timedelta, time
from django.db.models import Count
from issues.models import Bug, Feature
from django.http import JsonResponse

# Create your views here.


def chart(request):
    #     today = datetime.now().date()
    #     tomorrow = today + timedelta(1)
    #     today_start = datetime.combine(today, time())
    #     today_end = datetime.combine(tomorrow, time())
    #     completed_daily = Issue.objects.filter(resolved_date__gte=today_start).filter(resolved_date__lt=today_end).count()

    #     this_week_start = datetime.combine(today - timedelta(7), time())
    #     completed_weekly = Issue.objects.filter(resolved_date__gte=this_week_start).filter(resolved_date__lt=today_end).count()

    #     this_month_start = datetime.combine(today - timedelta(28), time())
    #     completed_monthly = Issue.objects.filter(resolved_date__gte=this_month_start).filter(resolved_date__lt=today_end).count()
    #     print(completed_daily)

    #  return render(request, "dashboard.html", {'completed_daily': str(completed_daily), 'completed_weekly': str(completed_weekly), 'completed_monthly': str(completed_monthly)})
    return render(request, "dashboard.html")


def get_issue_type_json(request):
    lables = ["Bugs", "Features"]
    count_bugs = Bug.objects.all().count()
    count_features = Feature.objects.all().count()
    data = {
        'lables': lables,
        'count': [count_bugs, count_features],
    }
    return JsonResponse(data)


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
    dataset = Bug.objects.values('upvotes', 'title').exclude(
        upvotes=0).order_by('upvotes')
    print(dataset)
    data = {
        'dataset': 'dataset',

    }

    return JsonResponse(data)


def get_feature_upvotes_json(request):
    lables = ["Todo", "Doing", "Done"]
    count = [10, 4, 1]
    data = {
        'lables': lables,
        'count': count,

    }

    return JsonResponse(data)
