
from project_app.page import login_page
import unittest


class test_login(unittest.TestCase):

    def setUp(self):
        user_name = "jeny"
        password = "ilovedogs"
        user = {user_name: [password]}

    def test_login_valid(self):
        user_name = "jeny"
        password = "ilovedogs"
        valid = login_page.valid_login(user_name, password)
        self.assertEqual(valid, True, msg="Valid login is valid")

    def test_login_invalid_password(self):
        user_name = "jeny"
        password = "ilovecats"
        valid = login_page.valid_login(user_name, password)
        self.assertEqual(valid, False, msg="Incorrect Password should return false")





