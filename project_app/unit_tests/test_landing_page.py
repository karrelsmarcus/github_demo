import project_app.views
from project_app.views import landing_page
from django.test import TestCase, Client
from project_app.models import MyUser


class landing_page_test(TestCase):
    test_client = None
    landing_page = None
    course_list = None
    sup = None

    def setUp(self):
        self.test_client = Client()
        self.landing_page = project_app.views.landing_page()
        self.sup = MyUser(user_name="test_sup", password="test_sup", permission=MyUser.SUP)
        self.sup.save()
        self.instructor = MyUser(user_name="test", password="test", permission=MyUser.PROF)
        self.sup.save()
        self.invalid = MyUser(user_name="test2", password="test2", permission=MyUser.TA)

    def test_get_options(self):
        temp = self.landing_page.options.get(self.sup.user_id)
        self.assertEqual(temp, 'landingPage.html', msg="Supervisor should return correct page")

    def test_get_options_instructor(self):
        temp = self.landing_page.options.get(self.instructor.user_id)
        self.assertEqual(temp, 'landingPage_instructor.html', msg="Instructor should return correct page")

    def test_get_options_none(self):
        temp = self.landing_page.options.get(None)
        self.assertEqual(temp, None, msg="None should return none")

    def test_get_options_invalid(self):
        temp = self.landing_page.options.get(self.invalid.user_id)
        self.assertEqual(temp, None, msg="Invalid user_id should return none")

    def test_get_options_type(self):
        temp = self.landing_page.options.get(0)
        self.assertEqual(temp, None, msg="Invalid type should return none")

