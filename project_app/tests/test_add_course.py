from django.test import TestCase, Client
from project_app.models import supervisor, course


# Create your tests here.
class add_course(TestCase):

    def setUp(self):
        self.test_client = Client()
        temp = supervisor(name="test_sup", password="test_password")
        temp.save()

    def test_add_course(self):
        resp = self.test_client.post("/", {"name": "test_sup", "password": "test_password"}, follow=True)
        resp = self.test_client.post("/landing", {"course page": True}, follow=True)
        course_resp = self.test_client.post("/course", {"name": "name", "number": "301", "section": "000"}, follow=True)
        self.assertEqual(course_resp.context["name"], "name", "new course name should exist in context")
        self.assertEqual(course_resp.context["number"], "301", "new course number should exist in context")
        self.assertEqual(course_resp.context["section"], "000", "new course section should exist in context")


class add_course_defects(TestCase):

    def test_add_course_confirm(self):
        pass
