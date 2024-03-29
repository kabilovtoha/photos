# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .serializers import ElasticPhotoSerializer
from .models import Photo

@receiver(pre_save, sender=Photo, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticPhotoSerializer(instance)
    obj.save()

@receiver(post_delete, sender=Photo, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticPhotoSerializer(instance)
    obj.delete(ignore=404)
