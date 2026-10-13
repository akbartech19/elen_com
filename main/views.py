
from django.shortcuts import render, redirect
from .models import Contact


def index_view(request):
    return render(request, 'index.html')


def index2_view(request):
    return render(request, 'index-2.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("contact")

    return render(request, 'contact.html')


def fashion_view(request):
    return render(request, 'fashion.html')


def photography_view(request):
    return render(request, 'photography.html')


def travel_view(request):
    return render(request, 'travel.html')
