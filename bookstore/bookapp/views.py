from django.shortcuts import render, redirect, HttpResponse
from .forms import RequestForm
from .models import Request as RequestModel

# Create your views here.
def index(request):
    return render(request, "index.html", context={})


def makeRequest(request):
    form = RequestForm()
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')  # Retrieve comment from the form
            existing_request = RequestModel.objects.filter(comment=comment).first()
            if existing_request:
                return redirect("failure_page")
            else:
                form.save()
                return redirect("success_page")
        
    context = {"form" : form}

    return render(request, "request.html", context)

def successPage(request):

    return render(request, "success_page.html", context={})

def failurePage(request):

    return HttpResponse("Already submitted!")

def catalogue(request):
    return render(request, "catalogue.html", context={})