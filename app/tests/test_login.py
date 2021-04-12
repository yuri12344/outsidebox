from app.views.login import login

def test_main():
    try_login = login()
    expected = "logado"
    assert expected == try_login
    