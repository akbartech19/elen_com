from django.db.models import Count, Q
from django.shortcuts import render, redirect
from .models import Contact, Article, AboutInfo, Newsletter, SiteContactInfo
from django.conf import settings
from django.core.mail import send_mail


def get_categories():
    categories = (
        Article.objects.exclude(category="")
        .values("category")
        .annotate(total=Count("id"))
        .order_by("category")
    )

    result = []

    for item in categories:
        result.append({
            "name": item["category"],
            "count": item["total"],
            "category": item["category"],
            "total": item["total"],
        })

    return result


def index_view(request):
    articles = Article.objects.order_by("-created_at")

    return render(request, "index.html", {
        "articles": articles,
        "categories": get_categories(),
    })


def index2_view(request):
    articles = Article.objects.order_by("-created_at")

    return render(request, "index-2.html", {
        "articles": articles,
        "categories": get_categories(),
    })


def about_view(request):
    about = AboutInfo.objects.first()

    return render(request, "about.html", {
        "about": about,
        "categories": get_categories(),
    })


def contact_view(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        return redirect("contact")

    contact_info = SiteContactInfo.objects.first()

    return render(request, "contact.html", {
        "contact_info": contact_info,
        "categories": get_categories(),
    })


def fashion_view(request):
    keyword = request.GET.get("keyword", "")

    articles = Article.objects.all()
    popular_articles = Article.objects.order_by("-created_at")[:3]

    if keyword:
        articles = articles.filter(
            Q(title__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(category__icontains=keyword)
        )

    articles = articles.order_by("-created_at")

    return render(request, "fashion.html", {
        "articles": articles,
        "categories": get_categories(),
        "keyword": keyword,
        "popular_articles": popular_articles,
    })


def photography_view(request):
    articles = Article.objects.filter(
        category="Photography"
    ).order_by("-created_at")

    return render(request, "photography.html", {
        "articles": articles,
        "categories": get_categories(),
    })


def travel_view(request):
    articles = Article.objects.filter(
        category="Travel"
    ).order_by("-created_at")

    return render(request, "travel.html", {
        "articles": articles,
        "categories": get_categories(),
    })





def newsletter_subscribe(request):
    if request.method != "POST":
        return redirect("fashion")

    email = request.POST.get("email", "").strip()

    if not email:
        print("EMAIL ERROR: Email formadan kelmadi")
        return redirect("fashion")

    subscriber, created = Newsletter.objects.get_or_create(email=email)

    print("NEWSLETTER EMAIL:", email)
    print("NEW SUBSCRIBER:", created)

    send_mail(
        "Welcome to Elen Newsletter",
        (
            "Salom!\n\n"
            "Elen newsletter xizmatiga obuna bo'ldingiz.\n"
            "Saytimizdagi yangi postlar haqida email orqali "
            "xabar olib turasiz.\n\n"
            "Obuna bo'lganingiz uchun rahmat!"
        ),
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

    print("EMAIL SENT: Django send_mail muvaffaqiyatli tugadi")

    return redirect("fashion")





def category_view(request, category_name):
    articles = Article.objects.filter(
        category__iexact=category_name
    ).order_by("-created_at")

    return render(request, "fashion.html", {
        "articles": articles,
        "categories": get_categories(),
        "keyword": "",
        "popular_articles": Article.objects.order_by("-created_at")[:3],
    })
