from django.test import TestCase, Client
from project_app.models import MyUser, course


class test_login(TestCase):

    test_client = None
    sup = None

    def setUp(self):
        self.test_client = Client()
        for i in range(5):
            temp = MyUser(name=i, password=i, user_id=0)
            temp.save()

    def test_correctname(self):
        for i in range(5):
            resp = self.test_client.post("/", {"name": i, "password": i}, follow=True)
            self.assertTemplateUsed("landingPage.html")

    def test_incorrect_name(self):
        resp = self.test_client.post("/", {"name": "12", "password": "1"}, follow=True)
        self.assertEqual(resp.context["message"], "invalid login credentials",
                         msg="incorrect username should display message")

    def test_incorrect_name_template(self):
        resp = self.test_client.post("/", {"name": "12", "password": "1"}, follow=True)
        self.assertTemplateUsed("loginPage.html")

    def test_incorrect_password(self):
        resp = self.test_client.post("/", {"name": "1", "password": "123"}, follow=True)
        self.assertEqual(resp.context["message"], "invalid login credentials",
                         msg="incorrect password should display message")

    def test_incorrect_password_template(self):
        resp = self.test_client.post("/", {"name": "1", "password": "123"}, follow=True)
        self.assertTemplateUsed("loginPage.html")

