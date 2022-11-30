import project_app.views
from project_app.views import landing_page
from django.test import TestCase, Client
from project_app.models import supervisor, course


class landing_page_test(TestCase):
    test_client = None
    landing_page = None
    course_list = None
    sup = None

    def setUp(self):
        self.test_client = Client()
        self.landing_page = project_app.views.landing_page()
        self.sup = supervisor(name="test_sup", password="test_sup", user_id=0)
        self.sup.save()

    def test_get_options(self):
        temp = landing_page.get_options(self.landing_page, self.sup)
        self.assertEqual(temp, 0, msg="Should return 0 for option id")

    def test_get_options_invalid(self):
        temp = landing_page.get_options(self.landing_page, self.sup)
        self.assertEqual(temp, -1, msg="Invalid user should return -1")
