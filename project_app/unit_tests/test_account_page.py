import project_app.views
from django.test import TestCase, Client
from project_app.models import MyUser, course


class test_account_page(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.account_page = project_app.views.add_account_page()
        self.sup = MyUser(user_name="test_sup", password="test_sup", permission=MyUser.SUP)
        self.sup.save()

    def test_valid_account(self):
        acc = self.account_page.create_account(user_name="test", password="test", permission=MyUser.INS)
        self.assertTrue(acc, msg="valid account should return true")

    def test_invalid_name(self):
        acc = self.account_page.create_account(user_name="thisusernameistoolongtopassvalidation",
                                               password="test", permission=MyUser.INS)
        self.assertFalse(acc, msg="invalid username should return false")

    def test_invalid_password(self):
        acc = self.account_page.create_account(user_name="test", password="thispasswordistoolongtopassvalidation",
                                               permission=MyUser.INS)
        self.assertFalse(acc, msg="invalid password should return false")

    def test_invalid_permission(self):
        acc = self.account_page.create_account(user_name="test", password="test", permission="ERR")
        self.assertFalse(acc, msg="invalid permission should return false")

    def test_duplicate(self):
        self.account_page.create_account(user_name="test", password="test", permission=MyUser.INS)
        acc = self.account_page.create_account(user_name="test", password="test", permission=MyUser.INS)
        self.assertFalse(acc, msg="duplicate account should return false")
