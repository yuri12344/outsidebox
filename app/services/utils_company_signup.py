signup_company_json_format = {
    "name": "",
    "email": "",
    "password": "",
    "phone": "",
    "description": "",
    "adress": "",
    "cpf/cnpj": "",
    "schedule": "",
}


def check_data(data):
    print("Ola", data)
    error_handling = ""
    try:
        print(data['name'])
    except KeyError:
        error_handling += """O campo nome 'name' não pode ser vazio """
        print(error_handling)
        return "Não tem NOME"

    return True
