from .models import Article


def category_context(request):
    context = {}

    context["categories"] = Article.CATEGORY_CHOICES

    return context