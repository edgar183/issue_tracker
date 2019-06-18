from django.shortcuts import render
from issues.models import Bug

# Create your views here.
def do_search(request):
    bugs = Bug.objects.filter(title__icontains=request.GET['q'])
    return render(request, "bugs.html", {"bugs": bugs})
