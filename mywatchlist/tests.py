from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class AppTest(TestCase):
    def test_app_url_exists1(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    def test_app_url_exists2(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    def test_app_url_exists3(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code,200)