from django.shortcuts import render

from .models import Product


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
