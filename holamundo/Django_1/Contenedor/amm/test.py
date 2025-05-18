from django.test import TestCase
from django.urls import reverse

class test1(TestCase):
    def test_num1(self):
        url = "/"
        request = self.client.get(url)
        self.assertEqual(request.status_code, 200)