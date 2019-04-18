from django.test import TestCase
from Tools.URLPath import url_about_teacherteam, url_about_yoga, url_about_location, url_about_course


# Create your tests here.
class AboutTestCase(TestCase):
    def test_visit_teacherteam(self):
        c = self.client
        response = c.get(url_about_teacherteam)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacherteamUI.html')

    def test_visit_yogamessage(self):
        c = self.client
        response = c.get(url_about_yoga)
        self.assertTemplateUsed(response, 'yogamessageUI.html')

    def test_visit_location(self):
        c = self.client
        response = c.get(url_about_location)
        self.assertTemplateUsed(response, 'aboutlocationUI.html')

    def test_visit_course(self):
        c = self.client
        response = c.get(url_about_course)
        self.assertTemplateUsed(response, 'aboutclassUI.html')
