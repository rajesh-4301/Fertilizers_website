from django.contrib import admin
from django.contrib.admin.sites import site
from Login_Signup.models import login_info,signup_info


class login_admin(admin.ModelAdmin):
    list_display=('email','password')
admin.site.register(login_info,login_admin)


class signup_admin(admin.ModelAdmin):
    list_display=('fullname','mobile','email','password','cpassword')
admin.site.register(signup_info,signup_admin)

