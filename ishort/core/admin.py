from django.contrib import admin
from .models import (
    User,
    PricingPlan,
    SubscribedUser,
)

# Register your models here.

@admin.register(User)
class UserAdminView(admin.ModelAdmin):
    list_display = [
        'email',
        'password', 
        'first_name', 
        'last_name', 
        'is_superuser', 
        'is_staff', 
        'is_active',
    ]


@admin.register(PricingPlan)
class PlanAdminView(admin.ModelAdmin):
    list_display = [
        'plan_id',
        'plan_name',
        'plan_price',
        'plan_duration',
        'plan_number_url',
        'plan_number_qr',
        'plan_api_access',
        'plan_details',
        'plan_subs_count',
        'plan_created_at',
        'plan_updated_at',
    ]

@admin.register(SubscribedUser)
class SubscribedUserAdminView(admin.ModelAdmin):
    list_display = [
        'user',
        'plan',
        'is_subscribed',
        'plan_subscribed_at',
    ]