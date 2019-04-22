from django.test import TestCase
from Tools.URLPath import url_index, url_index_customer, url_index_admin
from Database.models import Customer
from Tools.SessionManager import SessionManager


# Create your tests here.
class UserLoginTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username="test_customer", password="test_customer_password")

    def test_user_unlogined_visit_index(self):
        c = self.client
        response = c.get(url_index)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Index.html')

    def test_customer_visit_index(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = c.session
        sessionManager.setLogin('test_customer')
        response = c.get(url_index_customer)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CustomerIndex.html')

    def test_admin_visit_index(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = c.session
        sessionManager.setLogin('test_admin')
        response = c.get(url_index_admin)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AdminIndex.html')
