from django.shortcuts import render

def home(request):
  context = {'title': 'salom'}
  return render(request, 'pages/home.html', context)

def handler_404(request, exception):
    return render(request, 'pages/404.html', {})