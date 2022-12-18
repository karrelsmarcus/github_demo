from django.test import TestCase, Client
from project_app.models import MyUser, course


# Create your tests here.
class add_course(TestCase):

    temp = None

    def setUp(self):
        self.test_client = Client()
        self.temp = MyUser(user_name="test_sup", password="test_password", permission=MyUser.SUP)
        self.temp.save()
        self.test_client.post("/", {"name": "test_sup", "password": "test_password"}, follow=True)
        self.test_client.post("/home/", {"name": "test_sup", "view_courses": "View Courses"}, follow=True)

    def test_add_course_template(self):
        course_resp = self.test_client.post("/create", {"name": self.temp.user_name, "cname": "name", "cnum": "301"}, follow=True)
        self.assertTemplateUsed(course_resp, "addCourse.html")

    def test_add_course_back_template(self):
        self.test_client.post("/create", {"back": "back"}, follow=True)
        self.assertTemplateUsed("viewCourse.html")

    def test_add_course_database(self):
        self.test_client.post("/create", {"cname": "name", "cnum": "301", }, follow=True)
        self.assertEqual("name", course.objects.get(number="301").name, msg="new course should exist in database")

    def test_add_course_database(self):
        self.test_client.post("/create", {"name": self.temp.user_name, "cname": "name", "cnum": "301"}, follow=True)
        self.assertEqual("name", course.objects.get(number="301").get_name(), msg="Course should be added to database")


