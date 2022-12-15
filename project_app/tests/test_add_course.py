from django.test import TestCase, Client
from project_app.models import MyUser, course


# Create your tests here.
class add_course(TestCase):

    temp = None

    def setUp(self):
        self.test_client = Client()
        self.temp = MyUser(name="test_sup", password="test_password", user_id='0')
        self.temp.save()

    def test_add_course_template(self):
        self.test_client.post("/", {"name": "test_sup", "password": "test_password"}, follow=True)
        course_resp = self.test_client.post("/create", {"name": self.temp.name, "cname": "name", "cnum": "301", "snum": "000"}, follow=True)
        self.assertTemplateUsed(course_resp, "addCourse.html")

    def test_add_course_back_template(self):
        self.test_client.post("/", {"name": "test_sup", "password": "test_password"}, follow=True)
        self.test_client.post("/create", {"back": "back"}, follow=True)
        self.assertTemplateUsed("landingPage.html")

    def test_add_course_get(self):
        self.test_client.post("/", {"name": "test_sup", "password": "test_password"}, follow=True)
        self.test_client.post("/home", {"create": "create course"}, follow=True)
        self.test_client.post("/create", {"name": self.temp.name, "cname": "name", "cnum": "301",
                                          "snum": "000", "add": "Add Course"}, follow=True)
        self.test_client.post("/create", {"back": "back"}, follow=True)
        resp = self.test_client.get("/home", {"name": self.temp.name})
        temp = resp.context["courses"]
        self.assertEqual(type(temp), list, msg="should return list of courses")
