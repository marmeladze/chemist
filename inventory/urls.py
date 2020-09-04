from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api_index'),
    path('companies/', views.companies_listing, name='companies_listing'),
    path('companies/<uuid:uuid>/', views.company_items_listing, name='company_items_listing'),

]