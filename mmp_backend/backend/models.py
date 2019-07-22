from django.db import models

# Create your models here.



class IndividualCoupon(models.Model):
        id = models.IntegerField(primary_key=True)
        USERID=models.CharField(max_length=50)
        COUPONID=models.IntegerField(default=0)

        def __str__(self):
                return self.USERID

class Coupon(models.Model):
        id = models.IntegerField(primary_key=True)
        STORENAME=models.CharField(max_length=50)
        NAME=models.CharField(max_length=50)
        IMAGENAME=models.CharField(max_length=50)
        IMAGE=models.ImageField(default='media/default_image.jpg')

        def __str__(self):
                return self.NAME


class Store(models.Model):
        GPSX = models.CharField(max_length=50)
        GPSY = models.CharField(max_length=50)
        LARG_CATE = models.CharField(max_length=50)
        MID_CATE = models.CharField(max_length=50)
        SMALL_CATE = models.CharField(max_length=50)
        NAME = models.CharField(max_length=50)
        IMAGENAME = models.CharField(max_length=50)
        IMAGE = models.ImageField(default='media/default_image.jpg')
        def __str__(self):
                return self.NAME

class Place(models.Model):

        GPSX = models.CharField(max_length=50)
        GPSY = models.CharField(max_length=50)
        LARG_CATE = models.CharField(max_length=50)
        MID_CATE = models.CharField(max_length=50)
        SMALL_CATE = models.CharField(max_length=50)
        NAME = models.CharField(max_length=50)
        IMAGENAME = models.CharField(max_length=50)
        IMAGE = models.ImageField(default='media/default_image.jpg')

        def __str__(self):
                return self.NAME



class Test(models.Model):
	version = models.CharField(max_length=10)

	def __str__(self):
		return self.version
