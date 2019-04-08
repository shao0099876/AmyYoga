from django.test import TestCase,Client
from Database.models import Customer
# Create your tests here.
class UserLoginTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin",authoritySignal=True,password="test_admin_password")
        Customer.objects.create(username="test_customer",password="test_customer_password")
    def test_user_uplogined_visit(self):
        c=Client()
        response=c.get('/login/')
