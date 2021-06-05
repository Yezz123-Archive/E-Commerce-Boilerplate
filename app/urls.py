from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from products.views import products_fill
from accounts import urls as urlpatterns
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', products_fill, name='index'),
    url(r'^accounts/', include(urlpatterns)),
    url(r'^products/', include(urls_products)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^cart/', include(urls_cart)),
    url(r'^user/', include(urlpatterns)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]