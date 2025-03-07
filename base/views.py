from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'base/home.html', context)

def gadgets(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'base/gadgets.html', context)