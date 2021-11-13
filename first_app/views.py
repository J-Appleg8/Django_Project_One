from django.shortcuts import render
from django.http import HttpResponse

app_name = "first_app"


def index(request):
    return HttpResponse("Hello World!")
