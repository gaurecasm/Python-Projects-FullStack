from django.conf.urls import url

from .views import ProductListView,ProductSlugView
# ProductDetailView,


urlpatterns = [
	# url(r'^$', home_page, name='home_page'),
	# url(r'^about/$', about, name='about'),
	# url(r'^contact/$', contact, name='contact'),
	# url(r'^login/$', login_page, name='login'),
    url(r'^$', ProductListView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)$', ProductDetailView.as_view()),
	# url(r'^register/$', register_page, name='register'),
    url(r'^(?P<slug>[\w-]+)/$', ProductSlugView.as_view()),

    # url(r'^admin/', admin.site.urls),
]
