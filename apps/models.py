from django.db import models
from multiselectfield import MultiSelectField

import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models


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

class ResizeImageMixin:
    def resize(self, imageField: models.ImageField, size:tuple):
        im = Image.open(imageField)  # Catch original
        source_image = im.convert('RGB')
        source_image.thumbnail(size)  # Resize to size
        output = BytesIO()
        source_image.save(output,quality=200 ,format='PNG') # Save resize image to bytes
        output.seek(0)

        content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
        file = File(content_file)

        random_name = f'app/{uuid.uuid4()}.png'
        imageField.save(random_name, file, save=False)


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
    
    def save(self, *args, **kwargs):
        # if self.pk is None:
        #     self.resize(self.image, (192, 192))

        super().save(*args, **kwargs)