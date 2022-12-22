from project_app.course_methods import course_methods as cm
from django.test import TestCase, Client
from project_app.models import MyUser, course
import unittest


class create_courses_tests(TestCase):
    test_client = None
    course_list = None
    courses_page = None
    sup = None

    def setUp(self):
        self.test_client = Client()
        self.courses_page = cm()
        self.sup = MyUser(user_name="test_sup", password="test_sup", permission=MyUser.SUP)
        self.sup.save()
        self.course_list = [["CS", "361", self.sup],
                            ["CS", "431", self.sup]]

        for i in self.course_list:
            course(name=i[0], number=i[1], owner=i[2]).save()

    def test_create_course_valid(self):
        name = "tst"
        number = "tst"
        temp = self.courses_page.create_course(name, number, self.sup)
        self.assertEqual(temp, True, msg="Course that doesn't exist already should return true")

    def test_create_course_invalid(self):
        name0 = "tst"
        number0 = "tst"
        self.courses_page.create_course(name0, number0, self.sup)
        name = "tst"
        number = "tst"
        temp = self.courses_page.create_course(name, number, self.sup)
        self.assertEqual(temp, False, msg="course that exists already should return false")

    def test_name_length(self):
        name = "0000000000000000000000000000000000000000000000000000"
        number = "111"
        section = "111"
        temp = self.courses_page.create_course(name, number, self.sup)
        self.assertEqual(temp, False, msg="course name with length > 50 should return false")

    def test_number_length(self):
        name = "000000"
        number = "1111"
        temp = self.courses_page.create_course(name, number, self.sup)
        self.assertEqual(temp, False, msg="course number with length > 3 should return false")

    def test_no_owner(self):
        name = "tst"
        number = "tst"
        temp = self.courses_page.create_course(name, number, None)
        self.assertEqual(temp, False, msg="Should not create course with no owner")


class get_courses_user_tests(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.courses_page = cm()
        self.sup = MyUser(user_name="test_sup", password="test_sup", permission=MyUser.SUP)
        self.sup.save()
        self.course_list = [["CS", "361", self.sup],
                            ["CS", "431", self.sup]]

        for i in self.course_list:
            course(name=i[0], number=i[1], owner=i[2]).save()

    def test_get_valid(self):
        courses = self.courses_page.get_courses_user(self.sup)
        self.assertEqual(type(courses), list, msg="should return list of courses")

    def test_get_invalid(self):
        courses = self.courses_page.get_courses_user(None)
        self.assertEqual(courses, [], msg="invalid user should not return any courses")
