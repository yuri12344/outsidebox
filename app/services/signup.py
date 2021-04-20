json_to_register = {
    "name": "",
    "email": "",
    "password": "",
    "phone": "",
    "address": "",
    "city": "",
    "state": "",
    "cpf/cnpj": "",
    "schedule": "",
    "description": "",
}


class SignUp():
    def __init__(self, *args):
        self.try_register = self.do_verifications(*args)

    def do_verifications(self, user):
        data_user = dict(user)
        data_user = self.check_keys(data_user)
        return data_user

    def check_keys(self, data):
        for key in json_to_register:
            try:
                data.get(data[key])
            except KeyError:
                return {"error": f"Use this json format {json_to_register}"}
        return data
