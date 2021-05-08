
from django.http import HttpResponse
from django.shortcuts import render

from Store.models import Product

def home(request):
    products=Product.objects.filter(is_available=True)

    context={
        'products':products
    }

    return render(request,'home.html',context)