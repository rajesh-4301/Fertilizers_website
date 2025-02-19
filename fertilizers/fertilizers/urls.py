"""
URL configuration for fertilizers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from fertilizers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login_view,name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('signup/',views.signup),
    path('products/',views.products,name="products"),
    path('login.html/save_logininfo',views.display_logininfo,name="savelogin"),
    path('signup.html/save_signupinfo',views.display_signupinfo,name="savesignup"),
    path('products/bestdeals.html/',views.bestdeals_view),
    path('products/seasonal.html/',views.seasonal_view),
    path('products/todayoffers.html/',views.todayoffers_view), 
    path('items/',views.items_view), 
    path('details-page/<slug>', views.detailspage_view),
    path('inorganic/', views.inorganic_view),
    path('organic/', views.organic_view),
    path('liquid/', views.liquid_view),
    path('bio/', views.bio_view),
    path('about/', views.aboutus_view, name='about'),  
    path('dashboard/', views.dashboard_view, name='dashboard'),  
    path('editprofile/', views.editprofile_view, name='editprofile'),  
    path('viewprofile/', views.viewprofile_view, name='viewprofile'),  
    path('myorders/', views.myorders_view, name='myorders'),  
    path('payment/<slug>', views.payment_view),  
    path('feedback/', views.feedback_view, name='feedback'),  
    path('success/', views.success_view, name='success'),  
    path('contactus/', views.contactus_view, name='contactus'),  
    path('cart/', views.cart_view),  
    path('wishlist/', views.wishlist_view),
    path('save_review/',views.review_info,name="savereview"),
    path('savedfeedback/',views.feedback_info, name = "savefeedback"),
    path('save_contact/',views.contactus_info,name="savecontact"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('reset-password/<str:token>/', views.reset_password, name="reset_password"),
    
    
     
    
    
    
    
    
    
]

urlpatterns += staticfiles_urlpatterns()


