from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from inventory.models import Company


# def index(request):
#     companies = Company.objects.all()
#     l = len(companies)
#     names = " ".join([c.name for c in companies])
#     locs = " ".join([c.country for c in companies])
#     return HttpResponse(f"Hello, world: There are {l} companies in the database. <br/>\
#       they are  {names}<br />\
#       and they are based in {locs}</br>")



def index(request):
    last_companies = Company.objects.order_by('-pk')[:20]
    context = {'last_added_companies': last_companies}
    return render(request, 'inventory/index.html', context)