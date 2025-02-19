from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from Products.models import products_data,contactus,review,feedback

class products_admin(ImportExportModelAdmin, admin.ModelAdmin):  # Inheriting both classes
    list_display = ('product_brand','product_name','product_category','price_inr',
    'discount_price','percentage','currency','delivery_options','expiration_date',
    'packaging_type' ,'country_origin' ,'image_url','description_1','description_2',
    'customer_review1','customer_reviewer1','customer_review2','customer_reviewer2',
    'customer_review3','customer_reviewer3','customer_review4','customer_reviewer4',
    'available_size1' ,'available_size2','available_size3','available_size4',
    'additional_feature2','additional_feature3' ,'additional_feature1','npk_ratio',
    'details_slug',
    )

# Registering the model with the custom admin
admin.site.register(products_data, products_admin)

class admin_contactus(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message')
admin.site.register(contactus,admin_contactus)

class admin_review(admin.ModelAdmin):
    list_display = ('name', 'review', 'rate')
admin.site.register(review,admin_review)

class admin_feedback(admin.ModelAdmin):
    list_display = ('satisfaction','prod_looks','process','deliv_satisfy','cust_rate','suggestion','recommend','rating')
admin.site.register(feedback,admin_feedback)