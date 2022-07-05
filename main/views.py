from django.db.models import query
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Product, Image, Header


# Create your views here.

def index(response):
    all_products = Product.objects.all().order_by('-pk')
    product_list = [a for a in all_products]
    images = Image.objects.all()
    header = Header.objects.get(name="home")
    return render(response, template_name="main/home.html", context={"product_list" : product_list, "images" : images, "header" : header})

def products(response, slug):
    all_products = Product.objects.all().order_by('-pk')
    product_list = [a for a in all_products]
    header = Header.objects.get(name="products")
    try:
        product = Product.objects.get(slug=slug)
        images = Image.objects.filter(product_id__exact=product)
        return render(response, template_name="main/product.html", context={"product_list" : product_list, "product" : product, "images" : images, "header" : header})

    except Product.DoesNotExist:
        return HttpResponse("Product does not exists")

def search(request):
    all_products = Product.objects.all().order_by('-pk')
    header = Header.objects.get(name="products")
    images = Image.objects.all()
    product_list = [a for a in all_products]
    
    if request.method == "POST":
        searched = request.POST['search']
        search_results = Product.objects.filter(Q(title__contains=searched) | Q(desc__contains=searched)).order_by('-pk')
        return render(request, template_name="main/search.html", context={"product_list" : product_list, "searched" : searched, "search_results" : search_results, "images" : images, "header" : header})
    else:
        searched = ""
        search_results = []
        return render(request, template_name="main/search.html", context={"product_list" : product_list, "searched" : searched, "search_results" : search_results, "images" : images, "header" : header})
