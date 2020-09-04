from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('companies/<int:id>/drugs', views.drugs_by_company, name='drugs_by_company')
    # path('companies/', views.companies_list, name='companies_listing'),
]