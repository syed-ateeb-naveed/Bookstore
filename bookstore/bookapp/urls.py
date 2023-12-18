from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.makeRequest, name="request"),
    path('success/', views.successPage, name="success_page"),
]
