from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.urls import reverse

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn;t select a choice!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirecting the users.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
