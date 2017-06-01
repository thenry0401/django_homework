from django.shortcuts import render
from django.http import HttpResponse

def index(reqeuts):
    return HttpResponse("Hello world. You're at the polls index.")
