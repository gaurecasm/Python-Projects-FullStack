from django.db import models
import os
import random
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.urls import reverse 
# Create your models here.

def file_name_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def file_modi(instance,filename):
	new_file_name = random.randint(1,45684)
	name, ext = file_name_ext(filename)
	final_name = "{new_file_name}{ext}".format(new_file_name=new_file_name,ext=ext)
	return "products/{new_file_name}/{final_name}".format(new_file_name=new_file_name,final_name=final_name)

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)
	def featured(self):
		return self.filter(featured=True,active=True)

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model,using=self._db)
	def all(self):
		return self.get_queryset().active()
	def featured(self):
		return self.get_queryset().filter(featured=True)

	def get_by_id(self,id):
		qs = self.get_queryset(),filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

class Product(models.Model):
	title = models.CharField(max_length=110)
	slug = models.SlugField(blank=True,unique=True)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20,default=45.54 )
	image = models.ImageField(upload_to=file_modi, null=True, blank=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=False)

	objects = ProductManager()

	def get_absolute_url(self):
		return "/products/{slug}/".format(slug=self.slug)
	
	def __str__(self):
		return self.title


def product_pre_save_reciever(sender,instance,*args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_reciever,sender=Product)
