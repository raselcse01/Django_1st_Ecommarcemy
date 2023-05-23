
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.master, name='master'),
    path('', views.index, name='index'),

    path('signup/', views.signup, name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),

#addtocart
    path('cart/add/<int:id>', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>', views.item_increment, name='item_increment'),

    path('cart/item_decrement/<int:id>', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail, name='cart_detail'),

#contact
    path('contact_us/',views.contact_us, name="contact_us"),

#Checkout
    path('checkout/',views.checkout, name="checkout"),

#order page
    path('order/',views.yourorder, name="order"),

#product page
    path('product/', views.product_page, name="product"),

#product details
    path('product_detail/<str:id>/', views.product_detail, name="product_detail"),

#search
    path('search/', views.search, name="search")

 


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
