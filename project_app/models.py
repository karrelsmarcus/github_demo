from django.db import models


# user_id: supervisor = 0
#          instructor = 1


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
    permission = models.CharField(max_length=20, choices=user_permission, default=TA)


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
    starttime = models.CharField(max_length=20)
    endtime = models.CharField(max_length=20)

    def get_course(self):
        return self.course

    def get_number(self):
        return self.number

    def set_assignment(self, user):
        self.assignment = user
