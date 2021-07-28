from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from .models import question,choice
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list = question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    myquestion = get_object_or_404(question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': myquestion})

def results(request, question_id):
    myquestion = get_object_or_404(question, pk=question_id)
    return render(request, 'polls/results.html', {'question': myquestion})

def vote(request, question_id):
    myquestion = get_object_or_404(question, pk=question_id)
    try:
        selected_choice = myquestion.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': myquestion,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(myquestion.id,)))
