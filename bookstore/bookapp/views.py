from django.shortcuts import render, redirect
from .forms import RequestForm
from .models import Request

# Create your views here.

def makeRequest(request):
    form = RequestForm()
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        
    context = {"form" : form}

    return render(request, "request.html", context)

def successPage(request):

    return render(request, "success_page.html", context={})