from django.shortcuts import redirect
from project_app.models import supervisor, course

class landing_page:

    def get_options(self, user_name):
        pass


class courses_page:
    def get_courses(self, user_name):
        pass

    def create_course(self, course_name, section, number, instructor):
        pass

    def assign_instructor(self, course_number, instructor_name):
        pass
