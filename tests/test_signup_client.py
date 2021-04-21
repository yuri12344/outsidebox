import requests
import json


def test_signup_client():

    given = {
            "name": "Joe Doe",
            "email": "joedoe@gmail.com",
            "password": "123456",
            "phone": "11-33823061",
            "address": "Rua Joao Pedro 43",
            "city": "Sao Paulo",
            "state": "Sao Paulo"
    }

    expected = {
        "sucess": "User created with sucess"
        }
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    result = requests.post(
        'http://127.0.0.1:5000/client/', data=json.dumps(given), headers=headers)

    assert result.json() == expected
