from django.shortcuts import render, redirect
from django.views import View
from .models import *


class login_page(View):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']

        valid = self.validate_login(name, password)

        if valid:
            request.session["name"] = name
            return redirect("/home/")
        else:
            return render(request, "loginPage.html", {"message": "invalid login credentials"})

    def validate_login(self, user_name, password):
        """""Validates credentials of user attempting to log in
        
        :param user_name: the user name of the user attempting to log in
               password: the password of a user attempting to log in
        :rtype: boolean
        :return: false if user login is invalid, true if it is
        """""
        no_user = False
        bad_password = False
        try:
            u = MyUser.objects.get(user_name=user_name)
            bad_password = (u.password != password)
        except:
            no_user = True
        if no_user or bad_password:
            return False
        else:
            return True


class landing_page(View):
    options = {MyUser.SUP: "landingPage.html",
               MyUser.INS: "landingPage_instructor.html"}

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, self.options.get(u.permission), {"name": u.user_name, "user": u})

    def post(self, request):
        resp = request.POST.get("create")
        resp1 = request.POST.get("logout")
        u = MyUser.objects.get(user_name=request.session['name'])

        if resp1:
            return render(request, 'loginPage.html', {})

        if resp:
            return render(request, 'addCourse.html', {"name": u.user_name})


class view_courses_page(View):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        courses = self.get_courses(u)
        return render(request, 'viewCourse.html', {"name": u.user_name, "courses": courses})

    def post(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        resp = request.POST.get("create")
        resp1 = request.POST.get("back")

        if resp1:
            return redirect("/home/")

        if resp:
            return render(request, 'addCourse.html', {"name": u.user_name})

    def get_courses(self, user_name):
        """""Returns list of courses associated with current user

        :param user_name: the model of the current user
        :rtype: list
        :return: None when no courses associated to user
                 List of courses associated to user
        """""

        try:
            courses = list(course.objects.filter(owner=user_name))
            return courses
        except() as e:
            return None


class add_courses_page(View):
    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "addCourse.html", {"name": u.user_name})

    def post(self, request):
        sup = MyUser.objects.get(user_name=request.session["name"])
        resp = request.POST.get("Add Course")
        resp1 = request.POST.get("back")

        if resp != '':
            c = self.create_course(request.POST.get("cname"), request.POST.get("cnum"), sup)

        if resp1 != '':
            return redirect("/home/")

        return render(request, "addCourse.html", {"name": sup.user_name})

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


class add_section_page(View):
    def get(self, request):
        return render(request, "addSection.html", {'name': request.session['name']})

    def post(self, request):
        try:
            c = course.objects.get(request.POST.get("course"))
            u = MyUser.objects.get()


