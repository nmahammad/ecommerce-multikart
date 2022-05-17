"""multikart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from core.views import error_404, about, ContactView, faq, index
from accounts.views import profile
from user.views import forgetPwd
from django.conf import settings
from django.urls import include, path
from order.views import cart_products, checkout, order_success, wish_list
# from user.views import profile
from product.views import product,search,vendor, product_detail, CategoryListView
from accounts.views import CustomLoginView,ChangePasswordView, forget_password, register,MulticartLogoutView

from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path("api/", include('product.api.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('cart/' , cart_products),
    path('checkout/' , checkout ),
    path('order-success/' , order_success, name='order-success'),
    path('wishlist/' , wish_list),
    path('forgetpwd/', forgetPwd),
    path('login/' , CustomLoginView.as_view(), name='login'),
    path('password-change/' , ChangePasswordView.as_view(), name='password_change'),
    path('logout/', MulticartLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('error/' , error_404),
    path('about/' , about),
    path('contact/' , ContactView.as_view(), name='contact'),
    path('faq/' , faq),
    path('' , index, name="/"),
    path('register/' , register),
    path('forget-password/' , forget_password),
    path('category/' ,CategoryListView.as_view(),name='category'),
    path('product/' , product ,name='product'),              #in this page you can see the products
    path('search/' , search),                                #in this page you can filter and search peoducts
    path('vendor/' , vendor),                                #in this page you can see the vendor profile
    path('profile/' , profile),                              #in this page, contact and billing details models exist
    path('accounts/', include('accounts.urls')),   
    path('product/<int:id>/', product_detail, name='product_detail'),

 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



