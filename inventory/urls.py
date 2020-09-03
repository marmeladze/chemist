from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('companies/', views.companies_list, name='companies_listing'),
]