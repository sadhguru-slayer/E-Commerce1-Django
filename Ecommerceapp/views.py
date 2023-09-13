from math import ceil
from django.shortcuts import render,redirect
from django.contrib import messages
from Ecommerceapp.models import Contact,Product,OrderUpdate,Order,Categories,Brands,Price_Filter,Volume_Filter
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail
from math import ceil
from django.template.loader import render_to_string, get_template
from Ecommerceapp import keys
from django.conf import settings
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import razorpay
client=razorpay.Client(auth=("rzp_test_jTenA9rtqgpQjd", "7gYa1enM8ie1fCy5ACKjnQ01"))


def index(request):
    categor=Categories.objects.all()
    CAT=request.GET.get('categor')
    if CAT:
        prods = Product.objects.filter(product_categore=CAT)[:12]
    else:
        prods=Product.objects.all()[:25]

    params={
        'prods':prods,
        'categor':categor,
    }
    return render(request,'index.html',params)

def contact(request):
    if request.method=="POST":
        user_name=request.POST.get("name")
        user_email=request.POST.get("femail")
        user_subject=request.POST.get("subject")
        user_message=request.POST.get("message")
        myquery=Contact(name=user_name,subject=user_subject,email=user_email,message=user_message)
        contact_subject=user_subject
        contact_message=user_message
        email_from=settings.EMAIL_HOST_USER
        send_mail(contact_subject,contact_message,email_from,[user_email])
        myquery.save()
        messages='We will meet you soon...'
        params={
            'messages':messages
        }
        return render(request,"message_sent.html",params)

    return render(request,'contact.html')

def products(request):
    categories=Categories.objects.all()
    brands=Brands.objects.all()
    prices=Price_Filter.objects.all()
    volume=Volume_Filter.objects.all()
    # -------FILTERING---------
    CATID=request.GET.get('categories')
    BRAND_ID=request.GET.get('brands')
    PRICE_ID=request.GET.get('prices')
    VOLUME_ID=request.GET.get('volume')

    # ------SORTING----------
    ATOZ=request.GET.get('ATOZ')
    ZTOA=request.GET.get('ZTOA')
    PRICEL_H=request.GET.get('PRICEL_H')
    PRICEH_L=request.GET.get('PRICEH_L')
    # -----------------------
    if CATID:
        catprods = Product.objects.filter(product_categore=CATID)
    elif BRAND_ID:
        catprods = Product.objects.filter(product_brand=BRAND_ID)
    elif PRICE_ID:
        catprods = Product.objects.filter(Price_Filter=PRICE_ID)
    elif VOLUME_ID:
        catprods= Product.objects.filter(volume_filter=VOLUME_ID)
    elif ATOZ:
        catprods= Product.objects.all().order_by('name')
    elif ZTOA:
        catprods= Product.objects.all().order_by('-name')
    elif PRICEL_H:
        catprods= Product.objects.all().order_by('price')
    elif PRICEH_L:
        catprods=Product.objects.all().order_by('-price')
    else:
        catprods=Product.objects.all()

    params= {
        'catprods':catprods,
        'categories':categories,
        'brands':brands,
        'prices':prices,
        'volume':volume,
             }

    
    return render(request,'products.html',params)


@login_required(login_url="/auth/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/products/")


@login_required(login_url="/auth/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/auth/login/")
def item_clear_p(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/products/")


@login_required(login_url="/auth/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/auth/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/auth/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/auth/login/")
def cart_detail(request):
    return render(request, 'cart_detail.html')

def Search(request):
    searched_query=request.GET.get('query_pass')
    catprod=Product.objects.filter(name__icontains  = searched_query)
    params={
        'catprod':catprod,
       }
    
    return render(request,'search.html',params)

def Product_view(request,id):
    prod_view=Product.objects.filter(id=id).first()
    params={
        'prod_view':prod_view
    }
    return render(request,'product_view.html',params)

def checkout(request):
        if not request.user.is_authenticated:
            messages.warning(request,"Login & Try Again")
            return redirect('/auth/login/')
        else:
            data = ({ "amount": 500,
                    "currency": "INR",
                    'payment_capture':'1',
                    })
            payment = client.order.create(data=data)
            order_id=payment['id']
            params={
                'order_id':order_id,
                'payment':payment
            }
            return render(request, 'checkoutAll.html',params)
    
def Placeorder(request):
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        firstname=request.POST.get('Username')
        email=request.POST.get('Email')
        state=request.POST.get('State')
        city=request.POST.get('City')
        zip_code=request.POST.get('Zip-Code')
        additional_info=request.POST.get('Add_Info')
        address=request.POST.get('Address')
        phone=request.POST.get('phone')
        # amount=request.POST.get('amount')
        order_id=request.POST.get('order_id')
        # payment=request.POST.get('payment')
        order=Order(
            user=user,
            firstname=firstname,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            additional_info=additional_info,
            phone=phone,
            payment_id=order_id,
            # amount=amount,
        )
        order.save()
        return render(request,'place_order.html')
