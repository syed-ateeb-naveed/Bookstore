from django.shortcuts import render
from .forms import RequestForm
from .models import Request

# Create your views here.

def makeRequest(request):
    form = RequestForm()
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {"form" : form}

    return render(request, "request.html", context)