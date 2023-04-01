from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('author',views.author, name='author'),
    path('contact',views.contact, name='contact'),
    path('category',views.category, name='category'),
    path('tags',views.tags, name='tags'),
    path('single-post',views.single_post, name='single_post'),
    path('search',views.search, name='search'),
]