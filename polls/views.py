from django.template import loader
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from re import findall


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def search(request):
    return HttpResponse(loader.get_template('polls/search.html').render(request=request))


def searched(request):
    wanted = request.POST.get('wanted').lower().split()
    found_ids = []
    for question in Question.objects.all():
        title = str(question).lower()
        for word in wanted:
            if findall(".*" + word + ".*", title):
                found_ids.append(question.id)
    template = loader.get_template('polls/found.html')
    context = {
        'found_ids': found_ids,
        'questions': Question.objects.all()
    }
    return HttpResponse(template.render(context, request))

def add(request):
    return HttpResponse(loader.get_template('polls/add.html').render(request=request))


def check(requst):
    p = requst.POST.get
    print(p('count'))
    if p('title') and p('question') and \
        sum(bool(p('choice{}'.format(x))) for x in range(5)) >= 2:
            question = Question.objects.create(
                    title=p('title'),
                    question_text=p('question'),
                    pub_date=timezone.now(),
            )
            for x in range(int(p('count'))):
                c = p('choice{}'.format(x))
                if c:
                    question.choice_set.create(choice_text=c, votes=0)
            question.save()
            return redirect('/polls/{}'.format(question.id))
    else:
        return add(requst)