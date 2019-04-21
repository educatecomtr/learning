# learning/views/product.py
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from learning.models import Product
from django.core.exceptions import ObjectDoesNotExist


def product(request, pk=None):

    try:
        product_detail = Product.objects.get(pk=pk)
        context = {
            'product': product_detail
        }
        return render(request=request, template_name='product/detail.html', context=context)

    except ObjectDoesNotExist:
        return render(request=request, template_name='exceptions/notexists.html')


def products(request):

    product_list = Product.objects.order_by('-name')[:5]

    context = {
        'products': product_list
    }

    return render(request=request, template_name='product/list.html', context=context)


@require_http_methods(["GET", "POST"])
def product_archive(request, year=None, month=None):

    product_list = Product.objects.filter(created__year=year, created__month=month)

    context = {
        'year': year,
        'month': month,
        'products': product_list,
    }

    return render(request=request, template_name='product/archive.html', context=context)


