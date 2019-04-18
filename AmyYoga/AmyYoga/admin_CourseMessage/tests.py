from django.test import TestCase
from Database.models import *
from Tools.SessionManager import SessionManager


# Create your tests here.
class admin_CourseMessageTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username='test_customer', authoritySignal=False, password='test_customer_password')
        Course.objects.create(coursename='test_course', courseintroduction='test_course_introduction', courseprice=100,
                              course_flag=True)
        BuyRecord.objects.create(number=1, username='test_customer', coursename='test_course', amount=100,
                                 pay_flag=True, valid=True)
        BuyRecord.objects.create(number=2, username='test_customer', coursename='test_course', amount=100,
                                 pay_flag=False, valid=True)

    def test_admin_coursemessage_admin_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_admin')
        response = c.get('/admin_coursemessage/')
        self.assertTemplateUsed(response, 'coursemessageUI.html')
        courses = Course.objects.filter(course_flag=True)
        self.assertEqual(str(courses), str(response.context['order']))

    def test_admin_coursemessage_customer_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_customer')
        response = c.get('/admin_coursemessage/')
        self.assertEqual(response.content.decode(), '顾客禁止使用此功能')

    def test_Coursename_admin_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_admin')
        response = c.get('/admin_coursemessage/test_course')
        self.assertTemplateUsed(response, 'detailmessageUI.html')
        detailcourse = BuyRecord.objects.filter(coursename='test_course', valid=True)
        self.assertEqual(str(detailcourse), str(response.context['order1']))

    def test_Coursename_customer_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_customer')
        response = c.get('/admin_coursemessage/test_course')
        self.assertEqual(response.content.decode(), '顾客禁止使用此功能')

    def test_addcourse_admin_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_admin')
        response = c.get('/addcourse/')
        self.assertTemplateUsed(response, 'addcourseUI.html')

    def test_addcourse_customer_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_customer')
        response = c.get('/addcourse/')
        self.assertEqual(response.content.decode(), '顾客禁止使用此功能')

    def test_addcourse_admin_add(self):
        c = self.client
        oldCourses = Course.objects.filter(course_flag=True)
        tmp = str(oldCourses)
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_admin')
        response = c.post('/addcourse/',
                          {'coursename': 'test_addcourse', 'courseintroduction': 'test_addcourse_introduction',
                           'courseprice': 100}, follow=True)
        self.assertRedirects(response, "/admin_coursemessage/")
        courses = Course.objects.filter(course_flag=True)
        self.assertNotEqual(tmp, str(courses))

    def test_modifycourse_customer_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_customer')
        response = c.get('/modifycourse/')
        self.assertEqual(response.content.decode(), '顾客禁止使用此功能')
