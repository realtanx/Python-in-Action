from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("the polls index page")


def detail(request, qs_id):
    return HttpResponse("you're looking at question %s" %qs_id)


def results(request, qs_id):
    return HttpResponse("you're looking at the results of question %s" %qs_id)


def vote(request, qs_id):
    return HttpResponse("you're voting on question %s" %qs_id)