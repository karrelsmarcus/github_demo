from django.shortcuts import redirect


class login_page:

    valid_login = False


class courses_page:
    def get_courses(self, user_name):
        pass

    def create_course(self, course_name, section, number, instructor):
        pass

    def assign_instructor(self, course_number, instructor_name):
        pass



