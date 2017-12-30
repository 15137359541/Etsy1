
from django.db import models

# Create your models here.
class GoodsManager(models.Manager):
    pass

class Goods(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255,null=True)
    price_ago=models.FloatField(null=True)
    price_now = models.FloatField(null=True)
    feedback=models.FloatField(null=True)
    favorited=models.FloatField(null=True)
    img=models.FileField(upload_to='static/es_platform/img',null=True)
    good_url=models.CharField(max_length=255,null=True)
    shop_name=models.CharField(max_length=255,null=True)
    shop_url=models.CharField(max_length=255,null=True)
    shipping=models.CharField(max_length=255,null=True)
    label_one=models.CharField(max_length=255,null=True)
    label_two=models.CharField(max_length=255,null=True)
    source_time=models.CharField(max_length=255,null=True)

    goods_manage=GoodsManager()