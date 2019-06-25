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

# def get_issue_type_json(request):
#     bug_dataset = Bug.objects.values('type') \
#         .exclude(issue_type='') \
#         .annotate(total=Count('issue_type')) \
#         .order_by('issue_type')

#     chart = {
#         'chart': {'type': 'column'},
#         'title': {'text': 'Issue Type'},
#         'xAxis': {'type': "category"},
#         'series': [{
#             'name': 'Issue Type',
#             'data': list(map(lambda row: {'name': [row['issue_type']], 'y': row['total']}, dataset))
#         }]
#     }

#     return JsonResponse(chart)


def get_bug_status_json(request):
    dataset = Bug.objects.values('status').exclude(
        status='').annotate(total=Count('status')).order_by('status')
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Bug Status'},
        'series': [{
            'name': 'Bug Status',
            'data': list(map(lambda row: {'name': [row['status']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def get_feature_status_json(request):
    dataset = Feature.objects.values('status').exclude(
        status='').annotate(total=Count('status')).order_by('status')
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Feature Status'},
        'series': [{
            'name': 'Feature Status',
            'data': list(map(lambda row: {'name': [row['status']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)


def get_bug_upvotes_json(request):
    lables = ["Todo", "Doing", "Done"]
    count = [3, 4, 1]
    data = {
        'lables': lables,
        'count': count,

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
