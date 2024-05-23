from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
User = get_user_model()
class ListingUserOnline(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id',related_name='user_id')
    isOnline = models.BooleanField(default=False)
    firsttime_login = models.DateTimeField(null=True, blank=True)
    online_at = models.DateTimeField(null=True, blank=True)
    offline_at = models.DateTimeField(null=True, blank=True)


class CarouselPageIndex(models.Model):
    carouselIndex = models.IntegerField()
    path = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CarouselPageIndex'

class ProductionType(models.Model):
    ELECTRONICS_PRODUCT = "EP"
    CLOTHES_PRODUCT = "CP"
    SHOES_PRODUCT = "SP"
    STATUS_CHOICES = [
        (ELECTRONICS_PRODUCT, 'Gaming'),
        (CLOTHES_PRODUCT, 'Clothes'),
        (SHOES_PRODUCT, 'Shoes'),
    ]
    product_type = models.CharField(choices=STATUS_CHOICES,max_length=5)

class Product(models.Model):
    product_type_id = models.ForeignKey(ProductionType,on_delete=models.DO_NOTHING,db_column='product_type_id',related_name='product_type_id')
    name = models.CharField(max_length=300)
    color = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=1000000,null=True, blank=True)
    price = models.FloatField()
    folder_image = models.CharField(max_length=300)
    discount_percent = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
class ProductLike(models.Model):
    product_type_id = models.ForeignKey(ProductionType,on_delete=models.DO_NOTHING,db_column='product_id_like',related_name='product_id_like')
    user_like_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_like_id',related_name='user_like_id')
    like_count = models.IntegerField(default=0)
    rate_star = models.IntegerField(default=0)

class ProductComment(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product_id',related_name='product_id_comment')
    comment_user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='comment_user_id',related_name='comment_user_id')
    comment = models.CharField(max_length=100000)
    comment_at = models.DateTimeField(default=timezone.now,null=True,blank=True)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

class ReplyComment(models.Model):
    productcomment_id = models.ForeignKey(ProductComment,on_delete=models.CASCADE,db_column='productcomment_id',related_name='productcomment_id')
    reply_comment_user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='reply_comment_user_id',related_name='reply_comment_user_id')
    comment = models.CharField(max_length=100000)
    comment_at = models.DateTimeField(default=timezone.now,null=True,blank=True)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

class ProductOrder(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product_id',related_name='product_id_order')
    user_order_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_order_id',related_name='user_order_id')
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
