from django.shortcuts import render
from django.http import HttpResponse
from .models import question,choice
from django.http import Http404

# Create your views here.
def index(request):
    latest_question_list = question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        myquestion = question.objects.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': myquestion})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)