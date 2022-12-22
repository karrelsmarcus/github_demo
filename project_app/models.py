from django.db import models


class MyUser(models.Model):

    TA = 'TA'
    INS = 'Instructor'
    SUP = 'Supervisor'

    user_permission = (
        (TA, 'TA'),
        (INS, 'Instructor'),
        (SUP, 'Supervisor')
    )

    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=50, default="")
    permission = models.CharField(max_length=20, choices=user_permission, default=SUP)

    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_permission(self):
        if self.permission == 'SUP':
            return 'Supervisor'
        if self.permission == 'Instructor':
            return 'Instructor'

        return 'TA'




class course(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=3)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number


class section(models.Model):
    course = models.ForeignKey(course, on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    number = models.CharField(max_length=3)
    starttime = models.CharField(max_length=10)
    endtime = models.CharField(max_length=10)

    def get_course(self):
        return self.course

    def get_number(self):
        return self.number

    def get_time(self):
        return self.starttime + ' - ' + self.endtime

    def get_assignment(self):
        return self.assignment

    def set_assignment(self, user):
        self.assignment = user
