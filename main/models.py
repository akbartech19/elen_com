from django.conf import settings 
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Article(models.Model):
    CATEGORY_CHOICES = [
        ("Photography", "Photography"),
        ("Fashion", "Fashion"),
        ("Travel", "Travel"),
        ("Food", "Food"),
        ("Technology", "Technology"),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="articles/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name="Muallif",
    )

    def __str__(self):
        return self.title

class AboutInfo(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(
        max_length=200,
        default="Hello I'm"
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.user.username




class SiteContactInfo(models.Model):
    address = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.email



class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
