from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')


def articles_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='articles.html')


def article_details_page(request: HttpRequest, slug: str) -> HttpResponse:
    return render(request=request, template_name='details.html')


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html')


def contact_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='contact.html')
