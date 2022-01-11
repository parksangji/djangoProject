from django.shortcuts import render
from home.models import cat

# Create your views here.

def home(request):
    post_latest = cat.objects.order_by("-create_date")[:6]
    context = {
        "post_latest" : post_latest
    }
    return render(request,'home.html',context=context)