from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import Http404

from cart.models import Cart

from .models import Product
# Create your views here.
class ProductFeaturedListView(ListView):
	template_name = "products/featured-list.html"

	def get_queryset(self,*args, **kwargs):
		request = self.request
		return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
	queryset = Product.objects.all().featured()
	template_name = "products/list.html"

	# def get_queryset(self,*args, **kwargs):
	# 	request = self.request
	# 	return Product.objects.featured()




class ProductListView(ListView):
	# queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_queryset(self,*args, **kwargs):
		request = self.request
		return Product.objects.all()

class ProductDetailView(DetailView):
	# queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		pk= self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product does not exists")
		return instance

class ProductSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		try:

			instance = Product.objects.get(slug=slug, active=True)
		except Products.DoesNotExist:
			raise Http404("Not Found")
		except Product.MultipleObjectReturned:
			qs = Product.objects.filter(slug=slug,active=True)
			instance = qs.first()
		except:
			raise Http404("fuckkk")
		return instance
