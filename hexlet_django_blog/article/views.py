from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'articles.html',
        context={'tags': tags},
    )
