from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('request/', views.makeRequest, name="request"),
    path('success/', views.successPage, name="success_page"),
    path('failure/', views.failurePage, name="failure_page"),
]
