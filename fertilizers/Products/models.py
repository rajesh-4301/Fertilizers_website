from django.db import models
from autoslug import AutoSlugField
from django.utils.timezone import now

class products_data(models.Model):
    product_brand = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    price_inr = models.FloatField()
    discount_price = models.FloatField(default=0)
    percentage = models.IntegerField(default=0) 
    currency = models.CharField(max_length=30)
    delivery_options = models.CharField(max_length=100,default="No size available")
    expiration_date = models.DateField(auto_now=True) 
    packaging_type = models.CharField(max_length=50)
    country_origin = models.CharField(max_length=50)
    image_url=models.TextField(default="No image address given")
    description_1 = models.TextField()
    description_2 = models.TextField()
    customer_review1 = models.CharField(max_length=50,default="No review available")
    customer_reviewer1 = models.CharField(max_length=50,default="No review available")
    customer_review2 = models.CharField(max_length=50,default="No review available")
    customer_reviewer2 = models.CharField(max_length=50,default="No review available")
    customer_review3 = models.CharField(max_length=50,default="No review available")
    customer_reviewer3 = models.CharField(max_length=50,default="No review available")
    customer_review4 = models.CharField(max_length=50,default="No review available")
    customer_reviewer4 = models.CharField(max_length=50,default="No review available")
    available_size1 = models.CharField(max_length=100,default="No size available")
    available_size2 = models.CharField(max_length=100,default="No size available")
    available_size3 = models.CharField(max_length=100,default="No size available")
    available_size4 = models.CharField(max_length=100,default="No size available")
    additional_feature2 = models.TextField(default="No additional features available")
    additional_feature3 = models.TextField(default="No additional features available")
    additional_feature1 = models.TextField(default="No additional features available")
    npk_ratio = models.CharField(max_length=50)
    details_slug = AutoSlugField(populate_from='product_name', unique=True, null=True, default=None)

class contactus(models.Model):
    full_name = models.CharField(("Full Name"), max_length=50)
    email= models.EmailField(("Email"))
    message = models.TextField(("Message"))

class review(models.Model):
    name = models.CharField(("Name"), max_length=50)
    review = models.TextField(("Message"))
    rate = models.IntegerField(("Rating"))

class feedback(models.Model):
    satisfaction = models.CharField(("Overall Satisfaction"),max_length=20)
    prod_looks = models.CharField(("How was Product Looks"),max_length=10)
    process = models.CharField(("Process Experience"),max_length=20)
    deliv_satisfy = models.CharField(("Satisfaction about delivery options"),max_length=20)
    cust_rate = models.CharField(("Review about customer serviece"),max_length=20)
    suggestion = models.TextField(("Suggestions"), default=None, null=True)
    recommend = models.CharField(("Would you recomment the site"),max_length=10)
    rating = models.IntegerField(("Rating"))

