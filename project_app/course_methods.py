from project_app.models import *


class course_interface:

    def get_courses_all(self):
        pass

    def create_course(self, course_name, number, owner):
        pass

    def create_section(self, course, assignment, number, s_time, e_time):
        pass

    def get_courses_user(self, user):
        pass


class course_methods(course_interface):

    def get_courses_all(self):
        """""Returns list of courses associated with current user

        :param user: the model of the current user
        :rtype: list
        :return: None when no courses associated to user
                 List of courses associated to user
        """""

        try:
            courses = list(course.objects.all())
            return courses
        except() as e:
            return None

    def create_course(self, course_name, number, owner):
        """""Creates and adds a new course to the database, returns boolean

        :param course_name: the name of the course to be added, must be unique 
        :param number: the number of a course to be added, must be unique
        :param owner: the user object who is the owner of the course
        :rtype: boolean
        :return: true if course is added, false if it is not
        """""

        try:
            name = course.objects.get(name=course_name)

            if name is not None:
                return False
        except:
            if len(number) > 3 or len(course_name) > 50 or owner is None:
                return False

            new_course = course(name=course_name, number=number,
                                owner=owner)
            new_course.save()
            return True

        return False

    def create_section(self, course, assignment, number, s_time, e_time):

        try:
            n = section.objects.get(number=number)
            if n is not None:
                return False
        except:
            if course is None or assignment is None or len(number) > 3:
                return False

            new_section = section(course=course, assignment=assignment, number=number,
                                  starttime=s_time, endtime=e_time)
            new_section.save()

            return True

        return False

    def get_courses_user(self, user):
        """""Returns list of courses associated with current user

        :param user: the model of the current user
        :rtype: list
        :return: None when no courses associated to user
                 List of courses associated to user
        """""

        try:
            result = []
            courses = list(course.objects.filter(owner=user))

            for i in courses:
                sections = section.objects.filter(course=i)
                for j in sections:
                    result.append((i, i, j, j.assignment, j))
            return result
        except() as e:
            return None
