from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }
# In above code we used to do some settings in templates because we would like to view categories in all the nav's.
def all_products(request):
    products = Product.objects.all()
    return render(request , 'store/home.html',{'products': products})
    # in the dictionary field we are accessing the data from products that we accessed from the database

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/product_detail.html', {'product': product})