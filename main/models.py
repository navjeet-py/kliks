from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='images')
    title = models.TextField()
    user_email = models.EmailField()
    small_img = ResizedImageField(size=[1024, 1024], upload_to='small_img', null=True, blank=True, quality=80, force_format='JPEG')

    def __str__(self):
        return self.title


class ProfilePic(models.Model):
    pp = ResizedImageField(upload_to='profile_pics', size=[1000, 1000],
                           default='static_imgs/default_pp.jpeg', quality=90, force_format='JPEG')
    email = models.EmailField()

    def __str__(self):
        return self.email
