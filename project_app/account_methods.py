from project_app.models import *


class account_interface:

    def create_account(self, user_name, password, password1, permission, fname, lname):
        pass

    def get_accounts(self):
        pass

    def edit_account(self, email, phone, address, user):
        pass


class account_methods(account_interface):

    def create_account(self, user_name, password, password1, permission, f_name, l_name):

        try:
            name = MyUser.objects.get(user_name=user_name)

            if name is not None:
                return False
        except:
            if len(user_name) > 20 or len(f_name) > 20 or len(l_name) > 20 or len(
                    password) > 20 or permission is None or password != password1:
                return False

            if permission not in ('TA', 'Supervisor', 'Instructor'):
                return False

            new_account = MyUser(user_name=user_name, password=password, permission=permission, first_name=f_name,
                                 last_name=l_name)
            new_account.save()
            return True

        return False

    def get_accounts(self):
        try:
            accounts = list(MyUser.objects.all())
            return accounts
        except() as e:
            return None

    def edit_account(self, email, phone, address, user):
        user.set_email(email)
        user.set_phone(phone)
        user.set_address(address)
        user.save()
