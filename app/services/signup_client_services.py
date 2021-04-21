import re


def validate_data(client):
    return not [key for key in client if client[key] == "" or client[key] == None]


def validate_email(email):
    regex = r"^([\w\.\-]+)@([\w\-]+)((\.(\w){2,})+)$"
    return bool(re.match(regex, email))


def validate_password(password):
    # Minimo 6 digitos, 1 letra minuscula, 1 letra maiuscula, 1 numero, 1 caracter especial
    regex = r"(?=.*[a-z]){1,}(?=.*[A-Z]){1,}(?=.*[0-9]){1,}(?=.*[!@#$%^&*()--__+.]){1,}.{6,}$"
    return bool(re.match(regex, password))


json_to_register = {
    "name": "Joe Doe",
    "email": "joedoe@gmail.com",
    "password": "Min 3 character max 15",
    "phone": "00-000000000",
    "address": "Rua Henrique Anxieta",
    "city": "Sao Paulo",
    "state": "SP",
    "cpf/cnpj": "000.000.000-00",
    "schedule": "seg - sex 8 - 18",
    "description": "Descrição da sua empresa",
}


class SignUp():
    def __init__(self, *args):
        self.can_register = True
        self.try_register = self.check_data(*args)

    def check_data(self, user):
        json_data = dict(user)

        # Check KEYS
        json_data = self.check_keys(json_data)
        print(self.can_register)
        if self.can_register == False:
            return json_data

        # Check empty values
        json_data = self.check_empty_values(json_data)
        if self.can_register == False:
            return json_data

        # Check email
        json_data = self.check_if_the_email_is_written_correctly(json_data)
        if self.can_register == False:
            return json_data

        # Check password
        json_data = self.conditionally_validate_the_password(json_data)
        if self.can_register == False:
            return json_data

        if self.can_register == True:
            return json_data

    # Check keys

    def check_keys(self, json_data):
        for key in json_to_register:
            try:
                json_data.get(json_data[key])
            except KeyError:
                self.can_register = False
                return {"specific_error": f"{key} is missing", "Use this sample JSON": f"{json_to_register}"}
        self.can_register = True
        return json_data

    # Check empty values
    def check_empty_values(self, json_data):
        for key in json_data:
            if len(json_data[key]) == 0:
                self.can_register = False
                return {"specific_error": f"A {key} não pode está vazia(o)", "Use this sample JSON": f"{json_to_register}"}

        self.can_register = True
        return json_data

    # Check e-mail
    def check_if_the_email_is_written_correctly(self, json_data):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if (re.search(regex, json_data['email'])):
            self.can_register = True
            return json_data
        else:
            self.specific_error = "Problema no e-mail"
            self.can_register = False
            return {"specific_error": f"O email está errado", "Use this sample JSON": f"{json_to_register}"}

    def conditionally_validate_the_password(self, json_data):
        # Minimo 3 caracteres
        if len(json_data['password']) >= 3 and len(json_data['password']) <= 15:
            self.can_register = True
            return json_data
        if len(json_data['password']) < 3:
            self.can_register = False
            return {"specific_error": "A senha precisa ter no mínimo 3 caracteres e 15 no máximo", "Use this sample JSON": f"{json_to_register}"}

        return json_data
