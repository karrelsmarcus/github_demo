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
        # return render(request,'landingPage.html', {})

    def validate_login(self, user_name, password):
        """""Validates credentials of user attempting to log in
        
        :param user_name: the user name of the user attempting to log in
        :param password: the password of a user attempting to log in
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
        # u = MyUser.objects.get(user_name=request.session['name'])
        # return render(request, self.options.get(u.permission), {"name": u.user_name, "user": u})
        return render(request, "landingPage.html", {})

    def post(self, request):
        resp = request.POST.get("view_courses")
        resp1 = request.POST.get("logout")
        resp2 = request.POST.get("view_accounts")
        u = MyUser.objects.get(user_name=request.session['name'])

        if resp1:
            return render(request, 'loginPage.html', {})

        if resp2:
            return redirect("/accounts/")

        if resp:
            return redirect("/courses/")



class view_courses_page(View):

    def get(self, request):
        # u = MyUser.objects.get(user_name=request.session['name'])
        # courses = self.get_courses(u)
        # print(courses)
        return render(request, 'viewCourse.html', {})

    def post(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        resp = request.POST.get("create_course")
        resp1 = request.POST.get("back")

        if resp1:
            return redirect("/home/")

        if resp:
            return redirect("/create/")

    def get_courses(self, user):
        """""Returns list of courses associated with current user

        :param user: the model of the current user
        :rtype: list
        :return: None when no courses associated to user
                 List of courses associated to user
        """""

        try:
            courses = list(course.objects.filter(owner=user))
            return courses
        except() as e:
            return None


class add_courses_page(View):
    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "addCourse.html", {"name": u.user_name})

    def post(self, request):
        sup = MyUser.objects.get(user_name=request.session["name"])
        print(sup.user_name)
        resp = request.POST.get("add_course")
        resp1 = request.POST.get("back")

        if resp:
            c = self.create_course(request.POST.get("cname"), request.POST.get("cnum"), sup)
            print(c)

        if resp1:
            return redirect("/courses/")

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
        except:
            pass

    def create_section(self, course, assignment, number, s_time, e_time):

        try:
            n = section.objects.get(number=number)
            if n is not None:
                return False
        except:
            if course is None or assignment is None or len(number) > 3 or len(s_time) > 20 or len(e_time) > 20:
                return False

            new_section = section(course=course, assignment=assignment, number=number,
                                  starttime=s_time, endtime=e_time)
            new_section.save()

            return True

        return False



class account_page(View):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session["name"])
        a = self.get_accounts()
        return render(request, "viewAccount.html", {'name': u.user_name, 'accounts': a})

    def post(self, request):
        resp = request.POST.get("add_account")
        resp1 = request.POST.get("back")

        if resp:
            return redirect("/addaccount/")
        if resp1:
            return redirect("/home/")

    def get_accounts(self):
        try:
            accounts = list(MyUser.objects.all())
            return accounts
        except() as e:
            return None


class add_account_page(View):

    def get(self, request):

        return render(request, 'createAccount.html', {})

    def post(self, request):
        sup = MyUser.objects.get(user_name=request.session["name"])
        print(sup.user_name)
        resp = request.POST.get("submit")
        resp1 = request.POST.get("back")

        if resp:
            # c = self.create_course(request.POST.get("cname"), request.POST.get("cnum"), sup)
            # print(c)
            pass

        if resp1:
            return redirect("/accounts/")

        return render(request, "createAccount.html", {})



    def create_account(self, user_name, password, permission, f_name="", l_name="", email="", address="", phone=""):

        try:
            name = MyUser.objects.get(user_name=user_name)

            if name is not None:
                return False
        except:
            if len(user_name) > 20 or len(password) > 20 or len(f_name) > 20 or len(l_name) or len(email) > 50 or len(address) > 50 or len(phone) > 17:
                return False

            if permission not in (MyUser.SUP, MyUser.INS, MyUser.TA):
                return False

            new_account = MyUser(user_name=user_name, password=password, permission=permission, first_name=f_name, last_name=l_name, email=email, address=address, phone=phone)
            new_account.save()
            return True

        return False
