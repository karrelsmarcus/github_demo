from project_app.page import landing_page
import unittest
from django.test import TestCase, Client
from project_app.models import supervisor, course


class landing_page_test(TestCase):
    test_client = None
    course_list = None

    def setUp(self):
        self.test_client = Client()
        sup = supervisor(name="test_sup", password="test_sup", user_id=0)
        sup.save()

    def test_get_options(self):
        temp = landing_page.get_options("test_sup")
        self.assertEqual(temp, 0, msg="Should return 0 for option id")

    def test_get_options_invalid(self):
        temp = landing_page.get_options("test")
        self.assertEqual(temp, -1, msg="Invalid user should return -1")
