from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class City(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        ordering = ('name', )

    def __str__(self):
        return self.name


class Photo(models.Model):
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='uploads/%Y/%m', max_length=180, blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(400, 400)],
                                     format='JPEG',
                                     options={'quality': 90})
    desc = models.TextField(verbose_name=u'Описание', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')
        ordering = ('-id', )

    def get_image_thumbnail(self):
        if self.image:
            return f'{self.image_thumbnail.url}'
        return ''

    def get_detail_url(self):
        return f"{settings.BASE_URL}{reverse('photo-list')}{self.id}/"

    def get_username(self):
        if self.author:
            return self.author.get_username()
        return ''

    def __str__(self):
        return str(self.image)
