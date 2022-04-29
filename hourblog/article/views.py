from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import Article

def index(request):

    article = Article.objects.all()
    context = {'article': article }
    return render(request, 'index.html', context)


def one(request, pk):
    oneArticle = Article.objects.get(pk=pk)
    context = {
        'article': oneArticle
    }
    return render(request,'oneA.html', context)
