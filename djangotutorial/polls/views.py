from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question

# Create your views here.

def index(request):
    qs_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_questions": qs_list}
    return render(request, "polls/index.html", context)


def detail(request, qs_id):
    try:
        question = Question.objects.get(pk=qs_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, qs_id):
    return HttpResponse("you're looking at the results of question %s" %qs_id)


def vote(request, qs_id):
    return HttpResponse("you're voting on question %s" %qs_id)