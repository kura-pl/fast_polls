from django.shortcuts import render_to_response


def index(request):
    return render_to_response('fast_polls/index.html')


def contact(request):
    return render_to_response('fast_polls/contact.html')


def my_404(request):
    return render_to_response('fast_polls/404.html')
