from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from accounts.auth import admin_only


# Create your views here.

def demo(request):
    return HttpResponse("This is from demo app.")

@admin_only
def show_product(request):
    #to read all the data from database
    products = Product.objects.all()
    context = {
        'products' : products
    }

    return render(request, 'product/index.html', context)


@admin_only
def post_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Category Added')
            return redirect('/demo/addcategory')
        else:
            messages.add_message(request,messages.ERROR, 'Category Not Added')
            return render('/product /postcategory.html', {'form' : CategoryForm})



    context = {
        'form': CategoryForm
    }

    return render(request, 'product/postcategory.html', context)

@admin_only
def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product Added')
            return redirect('/demo/addproduct' )
        else:
            messages.add_message(request,messages.ERROR, 'Product Not Added')

            return render(request,'product/postproduct.html',{'form': ProductForm})
        
    return render(request,'product/postproduct.html', {'form':ProductForm })

@admin_only
def show_category(request):
    category = Category.objects.all()
    context = {
        'form': category
    }

    return render(request,'product/showcategory.html',context)

@admin_only
def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('/demo/showcategory')

@admin_only
def update_category(request, category_id):
    category = Category.objects.get(id = category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category Updated')
            return redirect('/demo/showcategory')
        else:
            messages.add_message(request,messages.ERROR, 'Category Not Updated')

            return render(request, 'product/updatecategory.html', context)
        
    context ={

            'form': CategoryForm(instance=category)
        }

    return render(request, 'product/updatecategory.html', context)

@admin_only
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'product Added')
            return redirect('/demo/showproduct')
        else:
            messages.add_message(request, messages.ERROR , 'Product Not Added')
            return render(request , 'product/updateproduct.html', {'form':ProductForm(instance=product)}) 


    return render(request , 'product/updateproduct.html', {'form':ProductForm(instance=product)})        
           


@admin_only
def delete_product(request, product_id):
    product = Product.objects.get( id=product_id)
    product.delete()
    messages.add_message(request, messages.ERROR, "Proudct deleted")
    return redirect('/demo/showproduct/')




