import pytest
from api_carrinho import app

@pytest.fixture()
def client():
    return app.test_client()

def test_index(client):
    resultado = client.get('http://127.0.0.1:5000/')
    assert resultado.status_code == 302

def test_adicionar_carrinho(client):
    resultado = client.get('http://127.0.0.1:5000/static/Carrinho.html')
    assert resultado.status_code == 200

def test_fechar_venda(client):
    resultado = client.get('http://127.0.0.1:5000/fecharVenda')
    assert resultado.status_code == 200