class UserValidation(object):
    def __init__(self, obj):
        self.object = obj

    @staticmethod
    def login_validation(login):
        try:
            if len(login) == 0:
                return 'Error: Login can not be empty'
            elif len(login) > 15 or len(login) < 4:
                return 'Error: Login should be more 4 or less 15 characters'
            elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(login):
                return 'Error: Login can not contains special characters'
            else:
                return login
        except SyntaxError:
            return 'Error: Login can not has value'

    @staticmethod
    def password_validation(password):
        try:
            if len(password) == 0:
                return 'Error: Password can not be empty'
            elif len(password) > 15 or len(password) < 4:
                return 'Error: Password should be more 4 or less 15 characters'
            elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(password):
                return 'Error: Password can not contains special characters'
            else:
                return password
        except SyntaxError:
            return 'Error: Login can not has value'

    @staticmethod
    def first_name_validation(fname):
        pass

    @staticmethod
    def last_name_validation(lname):
        pass

    def validation(self):
        errors = []
        data = [self.login_validation(self.object.get('login')),
                self.password_validation(self.object.get('password'))
                ]
        for i in range(len(data)):
            if "Error:" in data[i]:
                errors.append(data[i])

        if len(errors) != 0:
            return errors
        else:
            return None
