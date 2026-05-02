from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .db import Database
from .forms import GetArticlesQueryForm, WriteArticleForm


db = Database()


def home_page(request: HttpRequest) -> HttpResponse:
    articles = db.get_latest_articles()
    return render(request=request, template_name='home.html', context={'articles': articles})


def articles_page(request: HttpRequest) -> HttpResponse:
    form = GetArticlesQueryForm(request.GET)

    if form.is_valid():
        data = form.cleaned_data

        print(data)
        
        articles = db.find_articles_by_title(data['q'])

        return render(request=request, template_name='articles.html', context={'articles': articles})
    articles = db.get_articles()
    return render(request=request, template_name='articles.html', context={'articles': articles, 'form': form})


def article_details_page(request: HttpRequest, slug: str) -> HttpResponse:
    article = db.get_article_by_slug(slug)
    return render(request=request, template_name='details.html', context={'article': article})


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')


def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='contact.html')


def add_article_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request, template_name='add.html')
    elif request.method == 'POST':
        form = WriteArticleForm(request.POST)
        if not form.is_valid():
            return render(request=request, template_name='add.html', context={'form': form})

        title = request.POST.get('title')
        content = request.POST.get('content')
        db.add_article(title=title, content=content)
        return render(request=request, template_name='add.html', context={'message': 'Article added successfully!'})
    
