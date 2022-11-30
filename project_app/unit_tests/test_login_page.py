import project_app.views
from project_app.views import login_page
from django.test import TestCase, Client
from project_app.models import supervisor, course


class test_login(TestCase):
    test_client = None
    login_page = None

    def setUp(self):
        self.test_client = Client()
        self.login_page = project_app.views.login_page()
        temp = supervisor(name="jeny", password="ilovedogs", user_id=0)
        temp.save()

    def test_login_valid(self):
        user_name = "jeny"
        password = "ilovedogs"
        valid = login_page.validate_login(self.login_page, user_name, password)
        self.assertEqual(valid, True, msg="Valid login is valid")

    def test_login_invalid_password(self):
        user_name = "jeny"
        password = "ilovecats"
        valid = login_page.validate_login(self.login_page, user_name, password)
        self.assertEqual(valid, False, msg="Incorrect Password should return false")

    def test_login_invalid_username(self):
        user_name = "test"
        password = "test"
        valid = login_page.validate_login(self.login_page, user_name, password)
        self.assertEqual(valid, False, msg="Invalid username should return false")
