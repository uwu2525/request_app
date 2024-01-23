from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    return HttpResponse('Hello World')
def index(request):
    context = {'message': "Welcome my BBS",
               'members':["AAAさん", "BBBさん", "CCCさん"]}

    return render(request, 'request/index.html', context)
# Create your views here.
