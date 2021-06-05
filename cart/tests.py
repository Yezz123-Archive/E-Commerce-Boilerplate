from django.test import TestCase

from .views import adjust_cart
from django.urls import resolvers, reverse


class CartTest(TestCase):
    def test_cart_resolves(self):
        cart_page = resolvers('/cart/')
        self.assertEqual(cart_page.func, adjust_cart)
