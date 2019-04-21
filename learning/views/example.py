
from django.shortcuts import render
from django.views.decorators.http import *

def examples(request):
    return render(request=request, template_name='example/detail.html')

