from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def statistics(request):
    return render(request, 'pages/statistics.html')
