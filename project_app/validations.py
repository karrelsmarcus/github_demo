from project_app.models import *


class validation_interface:

    def validate_login(self, user_name, password):
        pass


class validation(validation_interface):

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
