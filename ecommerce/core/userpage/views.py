from django.shortcuts import render
from demo_app.models import *
from django.contrib.auth.decorators import login_required
from accounts.auth import *
from .models import *
from django.contrib import messages
from .forms import *


# Create your views here.

def  homepage(request):
    product=Product.objects.all()
    context = {
        'posts':product
    }

    return render(request, 'users/homepage.html',context)


def productdetail(request,product_id):
    product = Product.objects.get(id=product_id)
    context ={
        'form':product
    }
    return render(request,'users/productdetails.html',context)

def product(request):
    product = Product.objects.all()
    context = {
        'posts': product
    }
    return render(request,'users/products.html',context)


def contact(request):
    return render(request,'users/contactus.html')

@login_required
@user_only
def add_to_cart(request,product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    check_item_presence = Cart.objects.filter(user=user,product=product)
    if check_item_presence:
        messages.add_message(request, messages.ERROR ,"product already in cart")
        return redirect("/mycart")
    else:
        cart = Cart.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Item added to cart')
            return redirect('/mycart')
        else:
            messages.add_message(request, messages.ERROR, 'Item not added to cart')
            return redirect('/product')


@login_required
@user_only
def show_cart_items(request):
    user = request.user
    cart=Cart.objects.filter(user=user)
    context ={
        'cart': cart
    }

    return render(request, 'users/mycart.html', context)

@login_required
@user_only
def delete_cart_items(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    messages.add_message(request, messages.SUCCESS , 'Item Deleted From cart')
    return redirect('/mycart')

def order_form (request, product_id,cart_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            quantity = request.POST.get('quantity')
            price = product.product_price
            total_price = int(quantity)* int(price)
            contact_no = request.POST.get('contact_no')
            address = request.POST.get('address')
            payment_method = request.POST.get('payment_method')
            payment_status = request.POST.get('Payment_status')
            status = request.POST.get('status')
        order = Order.objects.create(
            Product = product,
            user =user,
            quantity = quantity,
            total_price =total_price,
            contact_no = contact_no,
            address = address,
            payment_method = payment_method,
            payment_status = payment_status,
            status =status
        )

        if order.payment_method == "Cash on Delivery":
            cart = Cart.objects.get(id=cart_id)
            cart.delete()
            messages.add_message(request, messages.SUCCESS, 'Order Successful')
            return redirect('/mycart')
        elif order.payment_method == 'esewa':
            context = {
                'order':order,
                'cart':cart
            }

            return render(request, 'users/esewa_payment', context)
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'users/orderpage.html', {'form': OrderForm})
            




    context = {
        'form': OrderForm
    }

    return render(request , 'users/orderpage.html',context)

