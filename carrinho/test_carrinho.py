import pytest
from api_carrinho import app
import requests

@pytest.fixture()
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_index_status_code(client):
    resultado = client.get('http://127.0.0.1:5000/')
    assert resultado.status_code == 302


# teste adicionar carrinho
def test_adicionar_carrinho(client):
    resultado = client.get('http://127.0.0.1:5000/static/Carrinho.html')
    assert resultado.status_code == 200


def test_adicionar_carrinho_produto(client):
    resultado = client.get('http://127.0.0.1:5000/adicionarCarrinho?produto=maça&quantidade=2')
    assert resultado.status_code == 302


# teste fechar venda
def test_fechar_venda_status_code(client):
    resultado = client.get('http://127.0.0.1:5000/fecharVenda')
    assert resultado.status_code == 200


# teste remover carrinho
def test_remover_carrinho_status_code(client):
    resultado = client.get('http://127.0.0.1:5000/static/removerCarrinho.html')
    assert resultado.status_code == 200


# teste mostrar itens do carrinho
def test_listar_carrinho_status_code(client):
    resultado = client.get('http://127.0.0.1:5000/listar/carrinho')
    assert resultado.status_code == 200
