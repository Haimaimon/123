from django.test import TestCase
from Job_Tech import models
# Create your tests here.

class URLTests(TestCase):
    #check urls of a local server pages
    def test_homepage(self):
        response=self.cilent.get('/')


    #check Register page
    def test_Register_Page(self):
        response = self.client.get('Register/')
        self.assertEqual(response.status_code, 404)

    #check General Register page
    def test_Success_Page(self):
        response = self.client.get('Success/')
        self.assertEqual(response.status_code, 404)

    #check Manager Register page
    def test_Reg_Page(self):
        response = self.client.get('Reg')
        self.assertEqual(response.status_code, 404)

