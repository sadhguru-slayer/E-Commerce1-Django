from Ecommerceapp import views
from django.urls import path

urlpatterns = [
    #Home
    path('',views.index,name="index"),
    #PRODUCTS
    path('products/', views.products, name="products"),
    path('contact/',views.contact,name="contact"),
    #CHECKOUT
    path('checkout/',views.checkout,name='checkout'),
    path('place_order/',views.Placeorder,name='Placeorder'),
#     path('handlerequest/', views.handlerequest, name="HandleRequest"),
    path('search/',views.Search,name='Search'),
    path('product_view/<str:id>',views.Product_view,name='Product_view'),
    #CART
    # path('cart_detail/',views.Cart,name='Cart'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_clear_p/<int:id>/', views.item_clear_p, name='item_clear_p'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
]
