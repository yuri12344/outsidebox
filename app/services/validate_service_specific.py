from flask import json
import os
from app.models.service_catalog_model import ServiceCatalogModel
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app.models.signup_client_model import ClientModel
import datetime
base_url = os.getenv('BASE_URL')


json_to_register = {
    "name_of_service": "Name of specific service",
    "client_name": "Client name",
    "id_client": "int - Optional",
    "price": "Service price",
    "service_description": "Short specific service description",
    "informations": "links or extra informations",
    "feedback": "*",
    "aproved": "Bool, True or False, if client aproved the service, put True, if is a budget, put False",
    "responsible": "Felipe"
}


class ValidateServiceSpecific():
    def __init__(self, *args):
        self.can_register = True
        self.specific_error = "0"
        self.name_of_service = ""
        self.client_name = ""
        self.id_client = ""
        self.price = ""
        self.service_description = ""
        self.informations = ""
        self.feedback = ""
        self.aproved = False
        self.responsible = ""
        self.date_time = ""
        self.validate_data = self.validate_data(*args)

    def validate_data(self, json):
        self.check_keys(json)
        self.check_name_of_service(json)
        self.check_client_name(json)
        self.check_id_client(json)
        self.check_price(json)
        self.check_service_description(json)
        self.check_informations(json)
        self.check_aproved(json)
        self.check_responsible(json)
        self.check_date_time()

        return "check"

    def check_keys(self, json):
        for key in json_to_register:
            try:
                json.get(json[key])
            except KeyError:
                self.can_register = False
                self.specific_error = f"{key} is missing, use this sample {json_to_register}"
        self.can_register = True
        return "checked"

    def check_name_of_service(self, json):
        if len(json['name_of_service']) == 0:
            self.can_register = False
            self.specific_error = "Name of service cannot be blank"
        self.name_of_service = json['name_of_service']

    def check_client_name(self, json):
        self.client_name = json['client_name']

    def check_id_client(self, json):
        if json['id_client'] == "":
            self.id_client = None
            self.feedback = "False"
            return "ok"
        if int(json['id_client']) != 0:
            client = ClientModel.query.filter_by(id=json['id_client']).first()
            if client:
                self.id_client = json['id_client']
                self.feedback = "True"
            if not client:
                self.id_client = None
                self.feedback = "False"

    def check_price(self, json):
        if len(json['price']) > 0 and len(json['price']) <= 25:
            self.price = json['price']
        else:
            self.can_register = False
            self.specific_error = "Your price need more then 0 caracters and below 25 caracters"

    def check_service_description(self, json):
        if len(json['service_description']) > 0 and len(json['service_description']) <= 255:
            self.service_description = json['service_description']
        else:
            self.can_register = False
            self.specific_error = "Your description need more then 0 caracter and below 255"

    def check_informations(self, json):
        if len(json['informations']) > 0 and len(json['informations']) <= 255:
            self.informations = json['informations']
        else:
            self.can_register = False
            self.informations = "Your informations need more then 0 caracter and below 255"

    def check_aproved(self, json):
        text_lower = json['aproved']
        text_lower = text_lower.lower()
        if text_lower == "false":
            self.aproved = False
        if text_lower == "true":
            self.aproved = True
        if text_lower != "false" and text_lower != "true":
            self.can_register = False
            self.specific_error = "In aproved, you need give True or False"

    def check_date_time(self):
        self.date_time = datetime.datetime.now()

    def check_responsible(self, json):
        self.responsible = json['responsible']
