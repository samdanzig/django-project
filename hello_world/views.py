from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page")
def index(request):
    if request.method == "POST":
       return HttpResponse("You must have POSTed something")
    else return HttpResponse(request.method)
           