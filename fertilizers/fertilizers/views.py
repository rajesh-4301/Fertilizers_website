from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from Login_Signup.models import login_info,signup_info
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from Products.models import products_data,review,contactus,feedback
from django.contrib.auth.forms import PasswordResetForm
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

'''1)Authenticate() used to verify the user credentials.takes user's credentials as arguments and checks if they match any
     existing user.
     
   2)login() function logs in a user by creating a session for them, includes:
      --> User submits login form
      --> Authentication
      --> Login
      --> Session Id sent to browser
      --> Session access
   3) User is Django's built-in user model that is part of the authentication framework.
      --> set_password(rawpassword): This method hashes the raw password and stores it in the password field'''
    

def index(request):
    return render(request,"index.html")

def login_view(request):
    try:
        if request.method == "POST":
            return HttpResponseRedirect('/signup.html/')  
    except: 
        pass
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login.html/')
def products_view(request):
    return render(request, "products.html")

def products(request):
    query = request.GET.get('p_title') 
    if query:
        products = products_data.objects.filter(product_name__icontains=query) 
    else:
        products = products_data.objects.all() 
    products = products[:4]
    return render(request, 'products.html',{'products':products})

def display_logininfo(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        terms_checked = request.POST.get('terms')
        remember_me = request.POST.get('remember_me')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')

        if not terms_checked:
            messages.error(request, 'You must agree to the terms and conditions to login.')
            return redirect('/login/')
        
        login(request, user)
        if remember_me: 
            request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            request.session.set_expiry(0) 
        return redirect('/products/')
    return render(request,"login.html")


def display_signupinfo(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        username = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        terms_checked = request.POST.get('terms')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username already taken!")
            return redirect('/signup/')
        
        if not terms_checked:
            messages.error(request,"You must agree to the terms and conditions to signup.")
            return redirect('/signup/')
        else:
            data_signup = signup_info(fullname=fullname,mobile=mobile,email=username,password=password,cpassword=cpassword)
            data_signup.save()
        
        if password != cpassword:
            messages.error(request,"Passwords do not match!")
            return redirect('/signup/')

        user = User.objects.create_user(username=username, first_name = fullname)
        user.set_password(password)
        user.save()
        # ✅ Send Welcome Email
        subject = "🎉 Congratulations! Your Account is Created"
        message = f"""
        Hello {fullname},\n\n
        Welcome to Fertilizers.com! 🎊 Your account has been successfully created.\n
        You can now log in and start shopping for the best fertilizers.\n\n
        Best Regards,\n
        Fertilizers Team 🌱
        """
        from_email = "fertilizersanytime11@gmail.com"  # Replace with your email
        recipient_list = [username]  # Since username is email
        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, "Account created successfully! Check your email for a welcome message.")
        except Exception as e:
            messages.warning(request, "Account created, but email could not be sent.")
        return redirect('/login/')    
    return render(request,"login.html")

def bestdeals_view(request):
    view_more=products_data.objects.all()
    if request.method=="GET":
        pt=request.GET.get('p_title')
        if pt!=None:
            view_more=products_data.objects.filter(product_name__icontains=pt)    
    dealsdata={
        'deals':view_more 
    }
    return render(request,'bestdeals.html',dealsdata)
def seasonal_view(request):
    view_more=products_data.objects.all()
    if request.method=="GET":
        pt=request.GET.get('p_title')
        if pt!=None:
            view_more=products_data.objects.filter(product_name__icontains=pt) 
    dealsdata={
        'deals':view_more
    }
    return render(request,'seasonal.html',dealsdata)
def todayoffers_view(request):
    view_more=products_data.objects.all()
    if request.method=="GET":
        pt=request.GET.get('p_title')
        if pt!=None:
            view_more=products_data.objects.filter(product_name__icontains=pt) 
    dealsdata={
        'deals':view_more
    }
    return render(request,'todayoffers.html',dealsdata)

def items_view(request):
    view_more=products_data.objects.all()
    if request.method=="GET":
        pt=request.GET.get('p_title')
        if pt!=None:
            view_more=products_data.objects.filter(product_name__icontains=pt) 
    dealsdata={
        'deals':view_more
    }
    return render(request,'items.html',dealsdata)

def detailspage_view(request,slug):
    details = products_data.objects.get(details_slug=slug)
    details_data = {
        'details_deals': details
    }
    return render(request, 'detailspage.html', details_data)

def aboutus_view(request):
    return render(request,"aboutus.html")

def dashboard_view(request):
    userdata=signup_info.objects.all()
    signup_data={
        'user_data':userdata
    }
    return render(request,"dashboard.html",signup_data)

def editprofile_view(request):
    return render(request,"editprofile.html")

def viewprofile_view(request):
    return render(request,"viewprofile.html")

def myorders_view(request):
    return render(request,"orders.html")

def payment_view(request,slug):
    if request.method == "POST":
        payment_method = request.POST.get("payment_method") 

        if not payment_method:  
            messages.error(request, "Please select a payment method before placing an order.") 
            return redirect("/payment/")  

        messages.success(request, f"Payment successful via {payment_method}!")  
        return redirect("/success/") 
    details = products_data.objects.get(details_slug=slug)
    details_data = {
        'details_deals': details
    }
    return render(request, 'payment.html', details_data) 

def cart_view(request):
    return render(request,'cart.html') 
def wishlist_view(request):
    return render(request,'wishlist.html')  
def feedback_view(request):
    return render(request,"feedback.html")
def success_view(request):
    return render(request,"success.html")
def contactus_view(request):
    return render(request,"contactus.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('/login/')


def organic_view(request):
    # Ensure organic_items is initialized with an empty queryset
    organic_items = products_data.objects.none()  
    # Get all Organic Fertilizer products by default
    if products_data.objects.filter(product_category="Organic Fertilizer").exists():
        organic_items = products_data.objects.filter(product_category="Organic Fertilizer")
    # If a search query is present, filter products based on the query
    pt = request.GET.get('p_title')
    if pt:
        organic_items = organic_items.filter(product_name__icontains=pt)
    return render(request, 'organic.html', {'category':organic_items})


def inorganic_view(request):
    inorganic_items = products_data.objects.none()
    if products_data.objects.filter(product_category="Chemical Fertilizer").exists():
        inorganic_items = products_data.objects.filter(product_category="Chemical Fertilizer")
    pt = request.GET.get('p_title')
    if pt:
        inorganic_items = inorganic_items.filter(product_name__icontains=pt)

    return render(request, 'inorganic.html', {'category': inorganic_items})

def bio_view(request):
    bio_items = products_data.objects.none()
    if products_data.objects.filter(product_category="Bio-Fertilizer").exists():
        bio_items = products_data.objects.filter(product_category="Bio-Fertilizer")
    pt = request.GET.get('p_title')
    if pt:
        bio_items = bio_items.filter(product_name__icontains=pt)

    return render(request,'bio.html', {'category': bio_items})

def liquid_view(request):
    liquid_items = products_data.objects.none()
    if products_data.objects.filter(packaging_type="Bottle").exists():
        liquid_items = products_data.objects.filter(packaging_type="Bottle")
    pt = request.GET.get('p_title')
    if pt:
        liquid_items = liquid_items.filter(product_name__icontains=pt)

    return render(request, 'liquid.html', {'category':liquid_items})

def review_info(request):
    view_more=products_data.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        reviews = request.POST.get('review')
        rate = request.POST.get('rating')
        print(rate)
        data = review(name=name, review=reviews, rate=rate)
        data.save()
    return redirect('/products/')

def feedback_info(request):
    if request.method == "POST":
        satisfaction = request.POST.get('satisfaction')
        prod_looks = request.POST.get('product_search')
        process = request.POST.get('checkout_process')
        deliv_satisfy = request.POST.get('delivery')
        cust_rate = request.POST.get('customer_service')
        suggestion = request.POST.get('suggestions')
        recommend = request.POST.get('recommendation')
        rating = request.POST.get('rate')
        data = feedback(satisfaction=satisfaction, prod_looks=prod_looks, process=process, deliv_satisfy=deliv_satisfy, cust_rate=cust_rate, recommend=recommend, rating=rating, suggestion = suggestion)
        data.save()
    return redirect('/products/')

def contactus_info(request):

    if request.method == "POST":

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        data = contactus(full_name=name, email=email, message=message)

        data.save()

    return  redirect('/products/')

reset_tokens = {}

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(username=email).first()
        
        if user:
            # Generate a secure reset token
            token = get_random_string(50)
            reset_tokens[email] = token  # Store token temporarily
            
            # Send reset email
            reset_link = request.build_absolute_uri(f"/reset-password/{token}/")
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: {reset_link}",
                "your-email@example.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "Reset link sent to your email!")
        else:
            messages.error(request, "Email not found!")
    
    return render(request, "forgot_password.html")

def reset_password(request, token):
    email = None
    for key, value in reset_tokens.items():
        if value == token:
            email = key
            break
    
    if not email:
        messages.error(request, "Invalid or expired reset link!")
        return redirect("forgot_password")

    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            user = User.objects.get(username=email)
            user.set_password(password)
            user.save()
            messages.success(request, "Password updated successfully!")
            return redirect("/login/")  # Redirect to login page
        else:
            messages.error(request, "Passwords do not match!")
    
    return render(request, "reset_password.html")

