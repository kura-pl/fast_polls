from django.template import loader
from .models import Question, Choice, Faq
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from re import findall
from random import choice
import matplotlib.pyplot as plt


def generate_png(labels, values):
    """Funkcja tworzaca wykres.
    :param values: wartosci liczbowe
    :param labels: etykiety
    """

    patches, texts = plt.pie(values)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('polls/static/chart.png', dpi=50, transparent=True)


def results(request, question_id):
    """Wyswietlanie wyników."""

    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    choices_texts, choices_votes = [], []
    for choice in choices:
        choices_texts.append(choice.choice_text)
        choices_votes.append(int(choice.votes))
    generate_png(choices_texts, choices_votes)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """Panel głosowania."""

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # unikanie ponownego głosowania przy nacisnieciu 'wstecz'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def index(request):
    """Przegląladarka obecnych pytan."""

    latest_question_list = Question.objects.order_by('-pub_date')  # sortowanie wedlug daty
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def search(request):
    """Ekran wyszukiwarki."""

    return HttpResponse(loader.get_template('polls/search.html').render(request=request))


def searched(request):
    """Wyswietlanie znalezionych ankiet."""

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
    """Ekran dodawania nowej ankiety."""

    return HttpResponse(loader.get_template('polls/add.html').render(request=request))


def check(request):
    """Ekran ankiety."""

    p = request.POST.get
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
        return add(request)


def get_random(request):
    """Losowanie ankiety."""

    question = choice(Question.objects.all())
    return redirect('/polls/{}'.format(question.id))


def get_faq(request):
    """Wyswietlanie FAQ."""

    template = loader.get_template('polls/faq.html')
    context = {
        'questions': Faq.objects.all()
    }
    return HttpResponse(template.render(context, request))