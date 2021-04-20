# Estrutura lógica das rotas

# 01 SIGNUP COMPANY
# url = /signup_company
# Método POST
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

data_to_register = {
    "name": "Mecanica do Pedro",
    "email": "mecanicadopedro@gmail.com",
    "password": "123456",
    "phone": "4198515949",
    "address": "Rua Paulo Silva 43",
    "city": "São José dos Pinhais",
    "state": "Parana",
    "cpf/cnpj": "860.402.201/12",
    "schedule": "seg-seg 8 as 18",
    "description": "Fazemos manutenção de carro e moto, completa e básica",
}

expected_return = {
    "sucess": "User created with sucess, please login in /login"
}

sample_missing_data = {
    "nam1e": "Mecanica do Pedro",  # Name escrito errado
    # ...etc
}

expected_return = {
    "error": "Use this json format {json_to_register}"
}
# END SIGNUP COMPANY


# 02 SERVICES CATALOG
# url = /services_catalog/create/<id_company >
# Método POST
# Vai receber o ID da empresa na URL
# Se id_company está logado
json_to_create_service_to_catalog = {
    "name": "Your generic service name",
    "price": 70,
    "description": "Short description",
    "id_company": 1  # int company ID given by URL
}

given_right_data = {
    "name": "Limpeza de bico",
    "price": 50,
    "description": "Limpeza de bico",
    "id_company": 1
}
expected = {
    "sucess": "Service created with sucess, id: {id_service}"
}

given_missing_data = {
    "nam1e": "Limpeza de bico",  # Name escrito errado
    # ...etc
}

expected = {
    "error": "Use this json format {json_to_create_service_to_catalog}"
}

# Se id_company não está logado
expected = {
    "error": "You cant acces this page"
}
# END SERVICES CATALOG


# 03 SERVICE REQUEST FROM CATALOG
# url = /catalog_service_request/<id_company >
# Método POST
# Se id_company está logado
json_to_create_service_request_from_catalog = {
    "id_service": "ID from created service in catalog ex: 1",
    "client_name": "Optional",
    "id_client": "Optional, if client have account put id_client here",
    "date/time": "2020-20-05",
    "informations": "links or extra informations",
    "feedback": "*",
    "aproved": "Bool, True or False, if client aproved the service, put True, if is a budget, put False",
    "responsible": "Felipe"
}
# * Se id_client existe gerar um link para dar feedback ex: "/feedback/<id_company>/<id_service>/<id_user>"
# se não existir setar para False

given = {
    "id_service": 1,
    "client_name": "Yuri Caetano",
    "id_client": 1,
    "date/time": "2020-20-05",
    "informations": "Cliente pediu para fazer orçamento, e iria consultar agenda depois",
    "feedback": "/feedback/1/1/1",  # Ex: /feedback/<id_company>/<id_service>/<id_user>
    "aproved": False,  # Orçamento foi aprovado ou não
    "responsible": "Felipe"
}

expected = {
    "sucess": "Sucess, you can check see service here: /get_services/<id_company>/<id_service>"
}

given_missing_data = {
    "id_service": 3,  # This company does not exists
    # ...etc
}

expected = {
    "error": "Use this json format {json_to_create_service_request_from_catalog}"
}

# Se id_company não está logado
expected = {
    "error": "You cant acces this page"
}
# END CATALOG SERVICE REQUEST


# 04 SPECIFIC SERVICE REQUEST
# url = /services_specific/create/<id_company>
# Se id_company está logado
# Método POST
json_to_create_specific_service_ = {
    "name_of_service": "Name of specific service",
    "client_name": "Client name",
    "id_client": "int - Optional",
    "price": "Service price",
    "service_description": "Short specific service description",
    "informations": "links or extra informations",
    "feedback": "*",
    "aproved": "Bool, True or False, if client aproved the service, put True, if is a budget, put False",
    "responsible": "Felipe",
    "id_company": "INT - id_company"
}
# * Se id_client existe gerar um link para dar feedback ex: "/feedback/<id_company>/<id_service>/<id_user>"
# se não existir setar para False

given = {
    "name_of_service": "Rebaixar o carro",
    "client_name": "Yuri Caetano",
    "id_client": 1,
    "price": 500,
    "date/time": "2020-20-05",
    "informations": "Vou precisar cortar um giro da mola",
    "feedback": "/feedback/1/2/1",  # /feedback/<id_company>/<id_service>/<id_user>
    "aproved": True,  # or false
    "responsible": "Felipe",
    "id_company": 1
}

expected = {
    "sucess": "Sucess, you can check service in this link: {/services_done/<id_company>/id_service}"
}

given_missing_data = {
    "id_company": 3  # This company does not exists
    # ...etc
}

expected = {
    "error": "Use this json format {json_to_create_specific_service_}"
}

# Se id_company não está logado
expected = {
    "error": "You cant acces this page"
}
# END CATALOG SERVICE REQUEST


# 05 GET SERVICES
# url = /get_services/<id_company>/<id_service>
# Método GET
# /get_services/1/1
# Caso o id_service existir no id_company
json_to_get_services = {
    "id_company": 1,
    "id_service": 1,
}

expected = {
    "client_name": "Yuri Caetano",
    "client_phone": "41-98555949",
    "date/time": "2020-20-05",
    "informations": "Fiz a limpeza vc pode ver aqui link, cuide do seu carro seguindo esse ex: link",
    "aproved": True,
    "responsible": "Felipe"
}

# Se for passado o json no formato errado
given_missing_data = {
    "id_company": 3,  # Company does not exists
    "id_service": 1,
}
expected = {
    "error": "Use this json format {json_to_get_services}"
}
# END GET SERVICES


# 06 UPDATE SERVICE
# url = /update_service/<id_company>/<id_service>
# Método UPDATE
# /update_service/1/1
# Se o id_company estiver logado, e id_service existir
json_to_update_services = {
    "name_of_service": "Name of service",
    "client_name": "Client name",
    "id_client": "int - Opcional, if client have account you put ID here",
    "informations": "links or extra informations",
    "feedback": "*",
    "aproved": "Bool, True or False, if client aproved the service, put True, if is a budget, put False",
    "responsible": "Felipe"
}

given = {
    "id_company": 1,  # Company does not exists
    "id_service": 1,
    "client_name": "Yuri Caetano",
    "id_client": 1,
    "date/time": "2020-20-05",
    "informations": "Cliente pediu para fazer orçamento, e iria consultar agenda depois, cliente aprovou e vou iniciar a limpeza, o cliente já trouxe o carro. Finalizei a limpeza, confira aqui: link",
    "feedback": "/feedback/1/1/1",  # /feedback/<id_company>/<id_service>/<id_user>
    "aproved": True,  # or false
    "responsible": "Felipe"
}

# Se for passado o json no formato errado
given_missing_data = {
    "id_company": 3,  # Company does not exists
    "id_service": 1,
    # etc...
}
expected = {
    "error": "Use this json format {json_to_request_services}"
}
# Se id_company não está logado
expected = {
    "error": "You cant acces this page"
}
# END UPDATE SERVICE


# 07 FEEDBACK
# url = /feedback/<id_company>/<id_service>/<id_user>
# Método POST
# Se id_user está logado
# Se usuário não deu feedback para este serviço
json_to_create_feedback = {
    "feedback": "A user feedback",
    "id_user": 1,
    "id_company": 1
}

give_right_feedback = {
    "feedback": "Thank you soo much, great company",
    "id_user": 1,
    "id_company": 1
}

expected = {
    "sucess": "Thank you for your feedback, you can see your feedback here: /companys/<id_company>"
}

give_wrong_feedback = {
    "feedback": "",
    "id_user": 1,
    "id_company": 1
}

expected = {
    "error": "Use this json format {json_to_create_feedback}"
}
# Se id_user não está logado
expected = {
    "error": "You cant acces this page"
}
# END FEEDBACK


# 08 company_dashboard
# Método GET
# url = /company_dashboard/<id_company>/
# Se id_company está logado
expected = {
    "company_name": "Mecanica do Pedro",
    "clients_list": ["Yuri Caetano", "Felipe"],
    "services_catalog": [{"service_name": "Limpeza de bico", "price": 50, "id_service": 1}],
    "link_create_service_catalog": "/services_catalog/create/<id_company>",
    "link_create_service_specific": "/services_specific/create/<id_company>",
    "company_profile": "/company/<id_company>"
}

# Se id_company não está logado
expected = {
    "error": "You cant acces this page"
}
# END company_dashboard


# 09 COMPANYS
# Método GET
# url = /companys/ ou
# url = /companys/<id_company>

# Caso id_company não seja informado
expected = {
    "companys_list": {
        {"company_1": {"name": "Mecanica do Pedro",
                       "company_profile": "/company/<id_company>"}},
        {"company_2": {"name": "Mecanica do Zé",
                       "company_profile": "/company/<id_company>"}},
    },
}

# Caso id_company informado seja 1
expected = {
    "company_name": "Mecanica do Pedro",
    "email": "mecanicadopedro@gmail.com",
    "phone": "4198515949",
    "addres": "Rua Paulo Silva 43",
    "city": "São José dos Pinhais",
    "state": "Parana",
    "cpf/cnpj": "860.402.201/12",
    "description": "Fazemos manutenção de carro e moto, completa e básica",
    "schedule": "seg-seg 8 as 18",
    "services_catalog": [{"service_name": "Limpeza de bico", "price": 50, "id_service": 1}],
    "feedbacks": ["Thank you soo much, great company", "Others"]
}
# Se o id não existir retornar erro
# END  COMPANYS


# 10 SIGNUP CLIENT
# url = /signup_client
# Método POST
sample_json_to_register = {
    "name": "Joe Doe",
    "email": "joedoe@gmail.com",
    "password": "123456",
    "phone": "11-33823061",
    "address": "Rua Joao Pedro 43",
    "city": "Sao Paulo",
    "state": "Sao Paulo",
}

given = {
    "name": "Joe Doe",
    "email": "joedoe@gmail.com",
    "password": "123456",
    "phone": "11-33823061",
    "address": "Rua Paulo Silva 43",
    "city": "Panambi",
    "state": "Sao Paulo",
}

expected_return = {
    "sucess": "User created with sucess"
}

given_missing_data = {
    "nam1e": "Joe Doe",
    "emai3l": "joedoe@gmail.com",
    "pass1word": "",
    "phone": "11-33823061",
    "address": "Rua Paulo Silva 43",
    "city": "",
    "state": "Sao Paulo",
}

expected_return = {
    "error": "Use this json format {sample_json_to_register}"
}
# END SIGNUP CLIENT


# 11 LOGIN
# url = /login
# Método POST

given = {
    "email": "yuuri.caetano@gmail.com",
    "password": "123456"
}

# Se na busca do e-mail ta tabela client bater
expected = {
    "redirect_url": "profile/<id_user>",
    "token": "asdaqwehuqwhuasaudh123"
}

# Se na busca do e-mail ta tabela company bater
expected = {
    "redirect_url": "company_dashboard/<id_user>",
    "token": "asdaqwehuqwhuasaudh123"
}

# Se o usuário não existir
expected = {
    "erro": "Senha ou login incorreto, ou crie sua conta"
}
# END LOGIN


# 12 CLIENT PROFILE
# url = /client_profile/<id_client>
# Método GET
# Se o id_client está logado
given = {
    "id_client": 1
}

expected = {
    "name": "Yuri Caetano",
    "email": "yuuri.caetano@gmail.com",
    "phone": "4133823061",
    "address": "Rua Henrique Gonzaga de Souza Neto, 407",
    "city": "São José dos Pinhais",
    "state": "Paraná",
    "services_done": [{}]
}
# Caso o usuário não esteja logado ou ID não existe
expected = {
    "erro": "Usuário inexistente ou faça login"
}
# END CLIENT PROFILE
