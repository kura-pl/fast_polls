from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('fast_polls/index.html')


def faq(request):
    return render_to_response('fast_polls/faq.html')


def contact(request):
    return render_to_response('fast_polls/contact.html')

