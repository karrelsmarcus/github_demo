from project_app.validations import validation as v
from django.test import TestCase, Client
from project_app.models import MyUser, course


class test_login(TestCase):
    test_client = None
    login_page = None

    def setUp(self):
        self.test_client = Client()
        self.login_page = v()
        temp = MyUser(user_name="jeny", password="ilovedogs", permission=MyUser.SUP)
        temp.save()

    def test_login_valid(self):
        user_name = "jeny"
        password = "ilovedogs"
        valid = self.login_page.validate_login(user_name, password)
        self.assertEqual(valid, True, msg="Valid login is valid")

    def test_login_invalid_password(self):
        user_name = "jeny"
        password = "ilovecats"
        valid = self.login_page.validate_login(user_name, password)
        self.assertEqual(valid, False, msg="Incorrect Password should return false")

    def test_login_invalid_username(self):
        user_name = "test"
        password = "test"
        valid = self.login_page.validate_login(user_name, password)
        self.assertEqual(valid, False, msg="Invalid username should return false")

    def test_invalid_type(self):
        username = []
        password = []
        valid = self.login_page.validate_login(username, password)
        self.assertEqual(valid, False, msg="should not accept incorrect type")
