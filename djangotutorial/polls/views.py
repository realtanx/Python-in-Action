from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    qs_list = Question.objects.order_by("-pub_date")[:5]
    out_put = ", ".join([q.question_text for q in qs_list])
    return HttpResponse(out_put)


def detail(request, qs_id):
    return HttpResponse("you're looking at question %s" %qs_id)


def results(request, qs_id):
    return HttpResponse("you're looking at the results of question %s" %qs_id)


def vote(request, qs_id):
    return HttpResponse("you're voting on question %s" %qs_id)