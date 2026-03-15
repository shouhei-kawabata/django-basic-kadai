from django.shortcuts import render
from django.views.generic import TemplateView, ListView,  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'


class ProductDetailView(DetailView):
    model = Product
    template_name = "crud/product_detail.html"

class ProductDetailView(DetailView):
    model = Product
    success_ur1 = reverse_lazy('list')    