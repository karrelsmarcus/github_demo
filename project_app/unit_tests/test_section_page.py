import project_app.views
from django.test import TestCase, Client
from project_app.models import MyUser, course


class test_section_page(TestCase):

    def setUp(self):
        self.test_client = Client()


