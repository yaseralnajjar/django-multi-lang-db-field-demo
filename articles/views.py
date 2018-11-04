from django.http import HttpResponse
from django.utils import translation

from .models import Article

def index(request):

    translation.activate('ar')
    article = Article.objects.all()[0]

    return HttpResponse(article.title)

def change(request):

    translation.activate('ar')
    article = Article.objects.all()[0]

    article.title.data['ar'] = 'مرحباً'
    article.save()

    return HttpResponse(article.title)