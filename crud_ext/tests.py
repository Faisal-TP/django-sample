from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class TestSample(TestCase):
    def setup(self):
        self.client = APIClient
    def test_index(self): #method name should start with test
        url = reverse('index')
        res = self.client.get(url)
        print(res.data)
        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.data, 'Congratulations, you have created an API')



