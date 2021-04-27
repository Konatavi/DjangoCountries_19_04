from django.contrib import admin
from django.urls import path
from CountriesApp import views

urlpatterns = [
    path('', views.main),
    path('countries-list/', views.countries),
    path('languages/', views.languages),
    # path('countries-list/<str:language>', views.countries_filter_by_lang),
    # path('countries-list/<str:word>', views.countries_filter_by_word),
    path('country/<str:country_name>', views.country_page),
]
