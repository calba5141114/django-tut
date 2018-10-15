from django.shortcuts import render
from django.http import HttpResponse as httpr
from django.http import Http404
from django.template import loader

from .models import Question

# Application Views


def index(request):
        # the list of questions from the databse
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # forming an obj to pass the template renderer
    context = {'latest_question_list': latest_question_list}
    # rendering the template.
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(" Question does not exist")
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    return httpr("Your looking at the results of question %s" % question_id)


def vote(request, question_id):
    return httpr("Your voitng on question %s" % question_id)
