from django.shortcuts import render,redirect
from myapp.models import Product
from .models import Cart

# Create your views here.
 
def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request, "cart/home.html", {"cart" : cart_obj })	

def cart_update(request):
	product_id = request.POST.get('product_id')
	# product_id = 8
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("show msg that [roduct doesn not exits")
			return redirect('cart:home')
		print(product_obj)
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj .products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session['cart_item'] = cart_obj.products.count()

	return redirect('cart:home')