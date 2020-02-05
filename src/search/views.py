from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from myapp.models import Product
# Create your views here.
class SearchProductView(ListView):
	template_name = "search/view.html"
	#storing the data the Query
	def get_queryset(self,*args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q', None)
		#if query contains somthing then use lookup & Q function and return karo PRoduct ke objects se filter krke
		if query is not None:
			lookups = Q(title__icontains=query) |Q(description__icontains=query)
			return Product.objects.filter(lookups).distinct()
		return Product.objects.all()