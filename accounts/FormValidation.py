import re


class FormValidation:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def nameValidation(self, name):
        pattern = "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
        result = re.match(pattern, name)

        if result:
            return True
        else:
            return False

    def userNameValidation(self, username):
        pattern = "^[[A-Z]|[a-z]][[A-Z]|[a-z]|\\d|[_]]{7,29}$"
        result = re.match(pattern, username)

        if result:
            return True
        else:
            return False

    def checkPasswordStrength(self, password):
        if len(password) < 6:
            return False
        return True

    def checkPasswords(self, pass1, pass2):
        if pass1 == pass2:
            return True
        return False
