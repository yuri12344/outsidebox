from flask import json
from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy
import os
from app.models.service_catalog_model import ServiceCatalogModel
from app.models.service_request_catalog_model import ServiceRequestCatalogModel
from app.models.signup_client_model import ClientModel
import datetime

base_url = os.getenv('BASE_URL')


json_to_register = {
    "id_service": "ID from created service in catalog ex: 1",
    "client_name": "Optional",
    "id_client": "Optional, if client have account put id_client here",
    "informations": "links or extra informations",
    "feedback": "*",
    "aproved": "Bool, True or False, if client aproved the service, put True, if is a budget, put False",
    "responsible": "Felipe"
}


class ValidateServiceRequestFromCatalog():
    def __init__(self, *args):
        self.can_register = False
        self.specific_error = "0"
        self.id_service = ""
        self.id_client = ""
        self.service_to_create = []
        self.client_name = ""
        self.date_time = ""
        self.informations = ""
        self.feedback = ""
        self.aproved = True
        self.responsible = ""
        self.validate_data = self.validate_data(*args)

    def validate_data(self, json):
        self.check_keys(json)
        self.check_id_service(json)
        self.check_id_client(json)
        self.check_client_name(json)
        # self.check_date_time()
        self.check_informations(json)
        self.check_feedback(json)
        self.check_aproved(json)
        self.check_responsible(json)
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

    def check_id_service(self, json):
        service = ServiceCatalogModel.query.filter_by(
            id=json['id_service']).first()
        if not service:
            self.can_register = False
            self.specific_error = "This id no exists, please give a real id or create one"
        if service:
            self.can_register = True
            self.service_to_create = service.__dict__
            self.id_service = json['id_service']

    def check_id_client(self, json):
        client = ClientModel.query.filter_by(id=json['id_client']).first()
        if client:
            self.id_client = json['id_client']
            self.feedback = "True"
        if not client:
            self.id_client = None
            self.feedback = "False"

    def check_client_name(self, json):
        self.client_name = json['client_name']

    def check_date_time(self):
        self.date_time = datetime.datetime.now()

    def check_informations(self, json):
        if len(json['informations']) == 0:
            self.can_register = False
            self.specific_error = "Informations cannot be blank"
        self.informations = json['informations']

    def check_feedback(self, json):
        client_logged = current_app.secret_key[2]['user']
        service_id = str(json['id_service'])
        id_user = str(self.id_client)
        client_loged_id = client_logged['id']

        url = base_url + "/feedback/" + \
            str(client_loged_id) + "/" + service_id + "/" + id_user

        if self.feedback == "True":
            self.feedback = url

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

    def check_responsible(self, json):
        self.responsible = json['responsible']
