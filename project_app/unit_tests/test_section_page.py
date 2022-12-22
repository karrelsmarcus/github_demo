from project_app.course_methods import course_methods as cm
from django.test import TestCase, Client
from project_app.models import MyUser, course


class test_section_page(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.section_page = cm()
        self.sup = MyUser(user_name="test_sup", password="test_sup", permission=MyUser.SUP)
        self.sup.save()
        self.ins = MyUser(user_name="test_ins", password="test_ins", permission=MyUser.INS)
        self.ins.save()
        self.course = course(name="Software Engineering", number="361", owner=self.sup)
        self.course.save()

    def test_valid_section(self):
        sec = self.section_page.create_section(self.course, self.ins, number="801",
                                               s_time="TR 9:30", e_time="10:20")
        self.assertTrue(sec, msg="valid section should return true")

    def test_invalid_course(self):
        sec = self.section_page.create_section(None, self.ins, number="801",
                                               s_time="TR 9:30", e_time="10:20")
        self.assertFalse(sec, msg="invalid course should return false")

    def test_invalid_ins(self):
        sec = self.section_page.create_section(self.course, None, number="801",
                                               s_time="TR 9:30", e_time="10:20")
        self.assertFalse(sec, msg="invalid instructor should return false")

    def test_invalid_number(self):
        sec = self.section_page.create_section(self.course, self.ins, number="8011",
                                               s_time="TR 9:30", e_time="10:20")
        self.assertFalse(sec, msg="invalid section number should return false")

    def test_valid_stime(self):
        sec = self.section_page.create_section(self.course, self.ins, number="801",
                                               s_time="TR 10:00", e_time="10:20")
        self.assertTrue(sec, msg="invalid start time should return false")

    def test_valid_etime(self):
        sec = self.section_page.create_section(self.course, self.ins, number="801",
                                               s_time="TR 9:30", e_time="10:20")
        self.assertTrue(sec, msg="invalid end time should return false")
