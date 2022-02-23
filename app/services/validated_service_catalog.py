import re

json_to_register = {
    "name_of_service": "Escreva o nome do seu serviço",
    "price": "00,00",
    "service_description": "Escreva a descrição do serviço"
}


class ValidatedServiceCatalog():
    def __init__(self, *args):
        self.can_register = True
        self.try_register = self.check_data(*args)

    def check_data(self, user):
        json_data = dict(user)

        # Check KEYS
        json_data = self.check_keys(json_data)
        if self.can_register == False:
            return json_data

        # Check empty values
        json_data = self.check_empty_values(json_data)
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
                return {"specific_error": f"A {key} não pode está vazia(o)",
                        "Use this sample JSON": f"{json_to_register}"}

        self.can_register = True
        return json_data


