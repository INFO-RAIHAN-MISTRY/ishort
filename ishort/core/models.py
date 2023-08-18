from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import (
    UserManager,
)
import random
import string

# Create your models here.

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class PricingPlan(models.Model):
    plan_id = models.CharField(max_length=50, blank=True, verbose_name='Plan Id auto generated')
    plan_name = models.CharField(max_length=50, verbose_name='Plan Name')
    plan_price = models.FloatField(default=0.0, verbose_name='Plan Price')
    plan_duration = models.IntegerField(verbose_name='Plan Duration in month')
    plan_number_url = models.BigIntegerField(default = 0, verbose_name='Number of urls')
    plan_number_qr = models.BigIntegerField(default = 0, verbose_name='Number of qr codes')
    plan_api_access = models.BooleanField(default = False)
    plan_details = models.TextField(verbose_name='Plan Details')
    plan_subs_count = models.BigIntegerField(default=0, verbose_name='Plan Subscribe Count')
    plan_created_at = models.DateField(auto_now=True)
    plan_updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        randomid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        self.plan_id = str(self.plan_name+'_'+randomid)
        super(PricingPlan, self).save(*args, **kwargs)

    def __str__(self):
        return self.plan_name

class SubscribedUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    plan = models.OneToOneField(PricingPlan, on_delete = models.CASCADE)
    is_subscribed = models.BooleanField(default = True)
    plan_subscribed_at = models.DateField(auto_now=True)

    def get_plan_name(request):
        SubscribedUser_obj = SubscribedUser.objects.get(user = request.user)
        return SubscribedUser_obj.plan