from django.db import models
from multiselectfield import MultiSelectField
from django.utils.text import slugify


platforms = (
        ('PWA', 'Progressive Web App'),
        ('IOS', 'Native IOS'),
        ('Android', 'Native android'),
        ('Flutter', 'Cross platform by Flutter'),
        ('Desktop Win', 'Native windows'),
        ('Desktop mac', 'Native macintosh'),
        ('Desktop Linux', 'Native linux')
    )


def image_upload(instance, filename):
    img_name, ext = filename.split(".")
    return f"media/app/{instance.id}.{ext}"

class Apps(models.Model): # table
    name = models.CharField(max_length=50,blank=False, unique=True)
    description = models.TextField(max_length=255, default='', blank=True)
    web_url = models.URLField(max_length=100, default='', blank=True)
    ios_url = models.URLField(max_length=100, default='', blank=True)
    android_url = models.URLField(max_length=100, default='', blank=True)
    desk_win_url = models.URLField(max_length=100, default='', blank=True)
    desk_mac_url = models.URLField(max_length=100, default='', blank=True)
    desk_lin_url = models.URLField(max_length=100, default='', blank=True)
    image = models.ImageField(upload_to=image_upload, default='', blank=True)
    last_update = models.DateTimeField(auto_now=True)
    published_time = models.DateTimeField(auto_now_add=True)
    platforms = MultiSelectField(choices=platforms)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comments(models.Model):
    name = models.CharField(max_length=50, default="", blank=True)
    content = models.TextField(max_length=255, default='', blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(Apps,related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.app.name} - {self.email}"

class vote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    suggestion = models.ForeignKey('Suggestion',related_name="votes", on_delete=models.CASCADE)
    vote_up = models.PositiveIntegerField(default=0)
    vote_down = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.suggestion.name}"


class Suggestion(models.Model):
    name = models.CharField(max_length=50, default="", blank=True)
    content = models.TextField(max_length=255, default='', blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(Apps,related_name="suggestions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.app.name} - {self.email}"