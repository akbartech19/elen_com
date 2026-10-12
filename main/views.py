from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index-2.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def fashion(request):
    return render(request, 'fashion.html')

def photography(request):
    return render(request, 'photography.html')

def travel(request):
    return render(request, 'travel.html')