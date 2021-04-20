signup_json_format = {
    "name": "",
    "email": "",
    "password": "",
    "phone": "",
    "adress": "",
    "city": "",
    "state": "",
}


class SignUp():
    def __init__(self, *args):
        self.user = self.do_verifications(*args)
        self.error = True

    def do_verifications(self, user):
        data_user = dict(user)
        data_user = self.check_name(data_user)
        print(data_user)
        return data_user

    def check_name(self, data):
        try:
            data.get('name')
            self.error = False
        except KeyError:
            self.error = True
            return {"ERRO": f"FALTA 'NAME'. USE O MODELO ABAIXO: {signup_json_format}"}
