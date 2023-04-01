from django.shortcuts import render

def home(request):
  context = {'title': 'Home'}
  return render(request, 'pages/home.html', context)

def author(request):
  context = {'title': 'Author'}
  return render(request, 'pages/author.html', context)

def contact(request):
  context = {'title': 'Contact'}
  return render(request, 'pages/contact.html', context)

def category(request):
  context = {'title': 'Category'}
  return render(request, 'pages/category.html', context)

def tags(request):
  context = {'title': 'Tags'}
  return render(request, 'pages/tags.html', context)

def single_post(request):
  context = {'title': 'Single Post'}
  return render(request, 'pages/single_post.html', context)

def search(request):
  context = {'title': 'Search'}
  return render(request, 'pages/search.html', context)

def handler_404(request, exception):
    return render(request, 'pages/404.html', {})