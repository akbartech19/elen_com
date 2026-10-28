
from django.conf import settings
from django.core.mail import send_mass_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article, Newsletter


@receiver(post_save, sender=Article)
def notify_newsletter_subscribers(sender, instance, created, **kwargs):
    if not created:
        return

    subscribers = Newsletter.objects.all()

    messages = []

    for subscriber in subscribers:
        subject = f"New post published: {instance.title}"

        message = (
            "Hello!\n\n"
            "A new post has been published on Elen.\n\n"
            f"Title: {instance.title}\n"
            f"Category: {instance.category}\n"
            f"Created at: {instance.created_at.strftime('%Y-%m-%d %H:%M')}\n\n"
            f"Details:\n{instance.content}\n\n"
            "Thank you for following Elen!"
        )

        messages.append((
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber.email],
        ))

    if messages:
        send_mass_mail(messages, fail_silently=False)
