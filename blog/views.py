from django.shortcuts import render

def home(request):
  context = {'title': 'Home'}
  return render(request, 'pages/home.html', context)

def contact(request):
  context = {'title': 'Contact'}
  return render(request, 'pages/contact.html', context)

def handler_404(request, exception):
    return render(request, 'pages/404.html', {})