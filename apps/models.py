from django.db import models
from multiselectfield import MultiSelectField

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
    return f"app/{instance.id}.{ext}"

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
    def __str__(self):
        return self.name
    