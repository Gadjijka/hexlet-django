from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
# Create your views here.

def article(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')

def original_view(request):
    reversed_url = reverse('article_show', kwargs = {'article_id': 42, 'tags': 'python'})
    return HttpResponseRedirect(reversed_url)
