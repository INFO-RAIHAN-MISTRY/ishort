from django.urls import path, include
from .views import (
    home,
    dashboard,
    check_url,
    manage_urls,
)

# app name ...
app_name = 'core'

urlpatterns = [
    #frontend Urls..
    path('', home, name='Home'),
    path('<slug>/', check_url, name="Check_Url"),

    # Dashboard Urls...
    path('user/dashboard/', dashboard, name="User_Dashboard"),
    path('user/manage-urls/', manage_urls, name="Manage_Urls"),
]
