from django.urls import path

from .views import (
    home_view,
    blogs_view,
    blog_detail_view,
)


urlpatterns = [
    path('', home_view, name='home_page'),
    path('blogs/', blogs_view, name='blogs_page'),
    path('blogs/<int:pk>', blog_detail_view, name='blog_detail_page'),
]
