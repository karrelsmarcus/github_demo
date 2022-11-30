import project_app.views
from project_app.views import courses_page
from django.test import TestCase, Client
from project_app.models import supervisor, course
import unittest


class get_courses_tests(unittest.TestCase):
    test_client = None
    course_list = None
    courses_page = None

    def setUp(self):
        self.test_client = Client()
        self.courses_page = project_app.views.courses_page()
        sup = supervisor(name="test_sup", password="test_sup", user_id=0)
        sup.save()
        self.course_list = {"test_sup": [["CS", 361, 801, None, "test_sup"], ["CS", 431, 802, None, "test_sup"]]}

        for i in self.course_list:
            course(name=i[0], number=i[1], section=i[2], instructor=i[3], supervisor=i[4]).save()

    def test_get_courses(self):
        temp = courses_page.get_courses(self.courses_page, "test_sup")
        self.assertEqual(temp, self.course_list.get("test_sup"), msg="Should return owners course list")
