from django.db import models
from core.models import (
    User
)
import random
import string

# Create your models here.

class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    short_url = models.CharField(max_length = 20, blank=True, verbose_name="Short Url Auto Generated")
    long_url = models.TextField(verbose_name="Long Url")
    url_title = models.CharField(max_length=100, verbose_name="Url Title")
    url_hit_count = models.PositiveIntegerField(default=0, verbose_name="Url Hit Count")
    url_created_at = models.DateField(auto_now=True)
    url_updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        random_short = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        self.short_url = str(random_short)
        super(Url, self).save(*args, **kwargs)
