from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from inventory.models import Company, Item
from inventory.serializers import CompanySerializer, ItemSerializer 

# def index(request):
#     companies = Company.objects.all()
#     l = len(companies)
#     names = " ".join([c.name for c in companies])
#     locs = " ".join([c.country for c in companies])
#     return HttpResponse(f"Hello, world: There are {l} companies in the database. <br/>\
#       they are  {names}<br />\
#       and they are based in {locs}</br>")



def index(request):
    api_index = {
      'companies': 'http://localhost:8000/inventory/companies',
      'ingredients': 'http://localhost:8000/inventory/ingredients',
    }
    return JsonResponse(api_index)

def companies_listing(request):
    companies = Company.objects.all()[:30]
    response = [CompanySerializer(company).to_dict() for company in companies]
    return JsonResponse(response, safe=False)

def company_items_listing(request, uuid=None):
    company = Company.objects.get(uuid = uuid)
    items = Item.objects.filter(company_uuid_id = uuid)

    response = {
      'company': CompanySerializer(company).to_dict(),
      'number_of_items': len(items),
      'items': [ItemSerializer(item).to_dict() for item in items]
    }
    return JsonResponse(response, safe=False)



