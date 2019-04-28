# learning/views/product.py
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from learning.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.generic import ListView, DetailView
from learning.forms import ProductForm
from django.http import HttpResponseRedirect


class ProductListView(ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'product/list.html'
    queryset = Product.objects.order_by('-name')[:2]
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_field'] = 'new field';

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ProductView(View):

    def get(self, request):
        context = {
            'products': self.get_queryset()
        }

        return render(request=request, template_name='product/list.html', context=context)

    def get_queryset(self):
        return Product.objects.order_by('-name')[:5]


'''
FUNCTION BASED VIEWS
'''


def products(request):

    product_list = Product.objects.order_by('-name')[:5]

    context = {
        'products': product_list
    }

    return render(request=request, template_name='product/list.html', context=context)


def product(request, pk=None):

    try:
        product_detail = Product.objects.get(pk=pk)
        context = {
            'product': product_detail
        }
        return render(request=request, template_name='product/detail.html', context=context)

    except ObjectDoesNotExist:
        return render(request=request, template_name='exceptions/notexists.html')


@require_http_methods(["GET", "POST"])
def product_archive(request, year=None, month=None):

    product_list = Product.objects.filter(created__year=year, created__month=month)

    context = {
        'year': year,
        'month': month,
        'products': product_list,
    }

    return render(request=request, template_name='product/archive.html', context=context)


def product_form(request):

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return HttpResponseRedirect('/learning/product/detail/%s/' % p.id)
    else:
        form = ProductForm()

    return render(request=request, template_name='product/add_product.html', context={'form': form})


def product_edit_form(request, pk=None):

    if request.method == "POST":
        instance = Product.objects.get(pk=pk)
        form = ProductForm(request.POST, instance=instance)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return HttpResponseRedirect('/learning/product/detail/%s/' % pk)
    else:
        p = Product.objects.get(pk=pk)
        form = ProductForm(instance=p)

    return render(request=request, template_name='product/add_product.html', context={'form': form})
