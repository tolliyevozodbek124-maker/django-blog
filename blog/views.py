from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def blogs_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Blogs Page</h1>')


def blog_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    return HttpResponse('<h1>Blog Detail Page</h1>')
