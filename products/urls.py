from django.conf.urls import url, include
from .views import products_fill

urlpatterns = [
    url(r'^$', products_fill, name='products')
    ]