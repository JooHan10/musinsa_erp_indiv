from django.shortcuts import render, redirect
from .models import ProductModel
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect("/product-list")
    else:
        return redirect("/sign-in")


@login_required
def product_list(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            all_products = ProductModel.objects.all().order_by('-created_at')
            return render(request, 'erp/product_list.html', {'products': all_products})
        else:
            return redirect("/sign-in")
    elif request.method == "POST":
        user = request.user
        products = ProductModel()
        products.author = user
        # products.


@login_required
def create_product(request):
    if request.method == "POST":
        user = request.user
        product_name = request.POST.get("product_name", None)
        product_code = request.POST.get("product_code", None)
        product_description = request.POST.get("product_description", None)
        product_price = request.POST.get("product_price", None)
        product_size = request.POST.get("product_size", None)

        exist_product = ProductModel.objects.filter(product_name=product_name)
        if exist_product:
            return render(request, 'erp/create_product.html')
        else:
            new_product = ProductModel()
            new_product.author = user
            new_product.product_name = product_name
            new_product.product_code = product_code
            new_product.product_description = product_description
            new_product.product_price = product_price
            new_product.product_size = product_size
            new_product.save()
            return redirect('/product-list')
    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/create_product.html')
        else:
            return render(request, "accounts/signin.html")
