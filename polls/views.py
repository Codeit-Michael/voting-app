from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from .models import question,choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = question
    template_name = 'polls/results.html'


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

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]