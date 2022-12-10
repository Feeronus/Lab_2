from django.shortcuts import render
from django import template
from django.http import HttpResponse
# Create your views here.
#def home(request):
    #return HttpResponse('Ohayo, sekai!\n')
    #return HttpResponse(u'Ohayo, sekai!\n', content_type="text/plain")
#def home(request):
    #return render(request, 'templates/index.html')
def home(request):
    return render(request, 'templates/static_handler.html')
