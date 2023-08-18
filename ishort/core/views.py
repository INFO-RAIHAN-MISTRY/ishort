from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import (
    User,
    PricingPlan,
    SubscribedUser,
)
from functions.models import (
    Url,
)

# Frontend View...

def check_url(request, slug):
    try:
        url_obj = Url.objects.get(short_url = slug)
        url_obj.url_hit_count = url_obj.url_hit_count+1
        url_obj.save()
        return redirect(url_obj.long_url)

    except Url.DoesNotExist:
        return redirect('core:Home')


def home(request):
    return render(request, 'index.html')



# Dashboard Views...

@login_required(login_url='account_login')
def dashboard(request):
    user = SubscribedUser.objects.get(user = request.user)
    context = {
        'user':user,
    }
    return render(request,'Dashboard/index.html', context)


@login_required(login_url='account_login')
def manage_urls(request):
    if request.method == "POST":
        user = request.user
        long_url = request.POST['long_url']
        url_title = request.POST['url_title']

        url_obj = Url.objects.create(
            user = user, 
            long_url = long_url,
            url_title = url_title,
        )

        if not url_obj:
            messages.error(request, 'Something went wrong, Try again ....')
            return redirect('core:Manage_Urls')

        messages.success(request, 'Short Url Generated Successfully ...')
        return redirect('core:Manage_Urls')

    url_obj_table = Url.objects.filter(user = request.user)
    context = {
        'urls': url_obj_table,
    }
    return render(request, 'Dashboard/manage-urls.html', context)