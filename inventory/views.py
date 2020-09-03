from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import Company


def index(request):
    companies = Company.objects.all()
    l = len(companies)
    names = " ".join([c.name for c in companies])
    locs = " ".join([c.country for c in companies])
    return HttpResponse(f"Hello, world: There are {l} companies in the database. <br/>\
      they are  {names}<br />\
      and they are based in {locs}</br>")