import re

def validate_data(client):

    # return client["name"] is None or client["name"] is ""
    if client["name"] == None or client["name"] == "":
        return False

    if client["phone"] == None or client["phone"] == "":
        return False
    if client["adress"] == None or client["adress"] == "":
        return False
    if client["city"] == None or client["city"] == "":
        return False
    if client["state"] == None or client["state"] == "":
        return False
    return True


def validate_email(email):
    regex = r"^([\w\.\-]+)@([\w\-]+)((\.(\w){2,})+)$"
    return bool(re.match(regex, email))


def validate_password(password):
    # Minimo 6 digitos, 1 letra minuscula, 1 letra maiuscula, 1 numero, 1 caracter especial
    regex = r"(?=.*[a-z]){1,}(?=.*[A-Z]){1,}(?=.*[0-9]){1,}(?=.*[!@#$%^&*()--__+.]){1,}.{6,}$"
    return bool(re.match(regex, password))
