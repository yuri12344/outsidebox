import requests
import json


def test_right_signup_company():

    given = {
        "name": "Mecanica do Pedro",
        "email": "mecanicadopedro@gmail.com",
        "password": "123456",
        "phone": "4198515949",
        "address": "Rua Paulo Silva 43",
        "city": "São José dos Pinhais",
        "state": "Parana",
        "cpf/cnpj": "860.402.201/12",
        "schedule": "seg-seg 8 as 18",
        "description": "Fazemos manutenção de carro e moto, completa e básica"
    }

    expected = {
        "try_register": {
            "name": "Mecanica do Pedro",
            "email": "mecanicadopedro@gmail.com",
            "password": "123456",
            "phone": "4198515949",
            "address": "Rua Paulo Silva 43",
            "city": "São José dos Pinhais",
            "state": "Parana",
            "cpf/cnpj": "860.402.201/12",
            "schedule": "seg-seg 8 as 18",
            "description": "Fazemos manutenção de carro e moto, completa e básica"
        },
        "can_register": "True"
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    result = requests.post(
        'http://127.0.0.1:5000/signup_company/', data=json.dumps(given), headers=headers)

    assert result.json() == expected
