import uuid
import base64
from django.db import models
from django.core.validators import URLValidator


HOST_NAME = 'http://localhost:8000/'


class Url(models.Model):
    url = models.CharField(max_length=256, validators=[URLValidator()])
    hash_url = models.CharField(max_length=10, unique=True, db_index=True)
    short_url = models.CharField(max_length=256, validators=[URLValidator()], blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save_url(self, *args, **kwargs):
        super(Url, self).save(*args, **kwargs)

    def hash_generator(self):
        hash = base64.urlsafe_b64decode(uuid.uuid1().bytes)[:8]
        hash_exist = Url.objects.filter(hash_url=hash)
        while hash_exist:
            hash = base64.urlsafe_b64decode(uuid.uuid1().bytes)[:8]
            hash_exist = Url.objects.filter(hash_url=hash)
            continue
        hash = hash.decode('utf-8')

    def short_url_creator(self):
        return HOST_NAME + self.hash_url
