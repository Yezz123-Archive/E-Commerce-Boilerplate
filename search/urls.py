from django.conf.urls import url
from .views import search_in

urlpatterns = [
    url(r'^$', search_in, name='search')
]