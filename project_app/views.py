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
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "landingPage.html", {'name': u.get_name(), 'role': u.get_permission(),
                                                    'address': u.get_address(), 'phone': u.get_phone(),
                                                    'email': u.get_email()})

    def post(self, request):
        resp = request.POST.get("view_courses")
        resp1 = request.POST.get("logout")
        resp2 = request.POST.get("view_accounts")
        resp3 = request.POST.get("edit_profile")
        print(resp3)
        u = MyUser.objects.get(user_name=request.session['name'])

        if resp1:
            return render(request, 'loginPage.html', {})

        if resp2:
            return redirect("/accounts/")

        if resp3:
            return redirect("/edit/")

        if resp:
            return redirect("/courses/")


class edit_account_page(View):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "editAccount.html", {'name': u.user_name})

    def post(self, request):
        resp = request.POST.get("back")
        resp1 = request.POST.get("confirm")

        if resp1:
            u = MyUser.objects.get(user_name=request.session['name'])
            e = request.POST.get("email")
            p = request.POST.get("pnum")
            a = request.POST.get("addr")
            print(u)
            print(e)
            print(p)
            print(a)
            self.edit_account(e, p, a, u)
            return redirect("/home/")

        if resp:
            return redirect("/home/")

    def edit_account(self, email, phone, address, user):
        user.set_email(email)
        user.set_phone(phone)
        user.set_address(address)
        user.save()


class view_courses_page(View):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        courses = self.get_courses(u)
        return render(request, 'viewCourse.html', {"courses": courses})

    def post(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        resp0 = request.POST.get("create_course")
        resp = request.POST.get("create_section")
        resp1 = request.POST.get("back")

        if resp1:
            return redirect("/home/")

        if resp:
            return redirect("/createSec/")

        if resp0:
            return redirect("/create/")

    def delete(self, request, number):
        c = section.objects.get(number=number)
        c.delete()
        return redirect('/courses/')

    def get_courses(self, user):
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


def delete_course(request, id):
    c = section.objects.get(id=id)
    c.delete()
    return redirect('/courses/')


def delete_account(request, id):
    a = MyUser.objects.get(id=id)
    a.delete()
    return redirect('/accounts/')


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
        accounts = self.get_accounts()
        courses = self.get_courses()
        return render(request, "addSection.html", {'name': request.session['name'], 'accounts': accounts, 'courses': courses})

    def post(self, request):

        resp = request.POST.get("back")
        print(resp)
        resp1 = request.POST.get("add")
        print(resp1)

        if resp:
            return redirect("/courses/")

        if resp1:
            c = course.objects.get(name=request.POST.get("course"))
            a = MyUser.objects.get(user_name=request.POST.get("account"))
            n = request.POST.get("snum")
            s = request.POST.get("stime")
            e = request.POST.get("etime")
            self.create_section(c, a, n, s, e)
            return redirect("/createSec/")

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

    def get_courses(self):
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

    def get_accounts(self):
        try:
            arr = []
            accounts = list(MyUser.objects.all())

            return accounts
        except() as e:
            return None


class view_account_page(View):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session["name"])
        a = self.get_accounts()
        return render(request, "viewAccounts.html", {'name': u.user_name, 'accounts': a})

    def post(self, request):
        resp = request.POST.get("create_accounts")
        resp1 = request.POST.get("back")

        if resp:
            return redirect("/createAcc/")
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

        return render(request, 'createAccount.html', {"permission_choice": MyUser.user_permission})

    def post(self, request):
        sup = MyUser.objects.get(user_name=request.session["name"])
        resp = request.POST.get("submit")
        resp1 = request.POST.get("back")

        if resp:
            user_name = request.POST.get("user_name")
            pw = request.POST.get("password")
            pw1 = request.POST.get("password1")
            perm = request.POST.get("permission")
            fname = request.POST.get("first_name")
            lname = request.POST.get("last_name")

            c = self.create_account(user_name, pw, pw1, perm, fname, lname)
            print(c)
            pass

        if resp1:
            return redirect("/accounts/")

        return render(request, "createAccount.html", {})

    def create_account(self, user_name, password, password1, permission, fname, lname):

        try:
            name = MyUser.objects.get(user_name=user_name)

            if name is not None:
                return False
        except:
            if len(user_name) > 20 or len(fname) > 20 or len(lname) > 20 or len(password) > 20 or permission is None or password != password1:
                return False

            if permission not in ('TA', 'Supervisor', 'Instructor'):
                return False

            new_account = MyUser(user_name=user_name, password=password, permission=permission, first_name=fname, last_name=lname)
            new_account.save()
            return True

        return False
