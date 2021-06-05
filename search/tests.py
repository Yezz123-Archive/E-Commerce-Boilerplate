from django.test import TestCase

from .views import do_search
from django.urls import resolvers, reverse
from django.shortcuts import render_to_response
 
class SearchTest(TestCase):
    def test_search_resolves(self):
        search_page = resolvers('/search/')
        self.assertEqual(search_page.func, do_search)