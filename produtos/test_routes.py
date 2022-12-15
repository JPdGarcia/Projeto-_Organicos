from decimal import Decimal

from database import mongo
from models import Produto, ProdutoPatchReq
from routes import listar_produtos, listar_um_produto, cadastrar_produto, atualizar_produto, deletar_produto


def test_cadastrar_produto_1():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": 1.99,
            "descricao": "Algumas bananas"}
    doc2 = {"doc_id": 99,
            "nome": "Maçã",
            "preco": "2.99",
            "descricao": "Algumas maçãs"}
    doc3 = {"_id": 1,
            "nome": "Goiaba",
            "preco": Decimal("3.99"),
            "descricao": "Algumas goiabas"}

    # Act
    product1 = cadastrar_produto(Produto(**doc1))
    product2 = cadastrar_produto(Produto(**doc2))
    product3 = cadastrar_produto(Produto(**doc3))
    product_list = [product1, product2, product3]

    # Assert
    for i, v in enumerate(product_list):
        assert isinstance(v, dict)
        assert "_id" not in v
        assert v["doc_id"] == i + 1
        assert isinstance(v["preco"], Decimal)
    
    # Cleanup
    mongo.coll.delete_many({})

def test_cadastrar_produto_2():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": 1.99,
            "descricao": "Algumas bananas",
            "opcional_lista": ["item1"],
            "opcional_dicionario": {"chave1": "valor1"},
            "opcional_subdocs": {"lista": [], "dicionario": {"c1": "v1"}, "decimal": 1.99}}

    # Act
    product1 = cadastrar_produto(Produto(**doc1))

    # Assert
    assert isinstance(product1["opcional_lista"], list)
    assert product1["opcional_lista"] == ["item1"]

    assert isinstance(product1["opcional_dicionario"], dict)
    assert product1["opcional_dicionario"] == {"chave1": "valor1"}

    assert isinstance(product1["opcional_subdocs"]["lista"], list)
    assert isinstance(product1["opcional_subdocs"]["dicionario"], dict)
    assert isinstance(product1["opcional_subdocs"]["decimal"], Decimal)
    
    # Cleanup
    mongo.coll.delete_many({})

def test_listar_produtos_1():
    # Arrange
    mongo.coll.delete_many({})

    # Act
    product_list = listar_produtos()

    # Assert
    assert product_list == []

def test_listar_produtos_2():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas"}
    doc2 = {"nome": "Maçã",
            "preco": Decimal("2.99"),
            "descricao": "Algumas maçãs"}
    doc3 = {"nome": "Goiaba",
            "preco": Decimal("3.99"),
            "descricao": "Algumas goiabas"}

    cadastrar_produto(Produto(**doc1))
    cadastrar_produto(Produto(**doc2))
    cadastrar_produto(Produto(**doc3))

    # Act
    product_list = listar_produtos()

    # Assert
    assert mongo.coll.count_documents({}) == 3
    assert isinstance(product_list, list)
    for product in product_list:
        assert isinstance(product, dict)

    # Cleanup
    mongo.coll.delete_many({})

def test_listar_um_produto():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas"}
    cadastrar_produto(Produto(**doc1))

    # Act
    product = listar_um_produto(doc_id=1)

    # Assert
    assert isinstance(product, dict)

    # Cleanup
    mongo.coll.delete_many({})

def test_atualizar_produto_1():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas"}
    cadastrar_produto(Produto(**doc1))

    update1 = {"nome": "Chocolate",
               "preco": Decimal("9.11"),
               "descricao": "Uma barra de chocolate"}

    # Act
    result1 = atualizar_produto(1, ProdutoPatchReq(**update1)).dict()

    # Assert
    assert result1["antes"]["nome"] == "Banana"
    assert result1["antes"]["preco"] == Decimal("1.99")
    assert result1["antes"]["descricao"] == "Algumas bananas"

    assert result1["depois"]["nome"] == "Chocolate"
    assert result1["depois"]["preco"] == Decimal("9.11")
    assert result1["depois"]["descricao"] == "Uma barra de chocolate"

    assert result1["antes"]["doc_id"] == result1["depois"]["doc_id"]

def test_atualizar_produto_2():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas"}
    cadastrar_produto(Produto(**doc1))

    update1 = {"lista": ["item1"]}

    # Act
    result1 = atualizar_produto(1, ProdutoPatchReq(**update1)).dict()

    # Assert
    assert "lista" not in result1["antes"]
    assert "lista" in result1["depois"]
    assert isinstance(result1["depois"]["lista"], list)
    assert result1["depois"]["lista"][0] == "item1"

def test_atualizar_produto_3():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas",
            "lista": ["item1"]}
    cadastrar_produto(Produto(**doc1))

    update1 = {"lista": ["item2"]}

    # Act
    result1 = atualizar_produto(1, ProdutoPatchReq(**update1)).dict()

    # Assert
    assert result1["antes"]["lista"] == ["item1"]
    assert result1["depois"]["lista"] == ["item1", "item2"]

def test_atualizar_produto_4():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas",
            "dicionario": {"chave1": "valor1"}}
    cadastrar_produto(Produto(**doc1))

    update1 = {"dicionario": {"chave2": "valor2"}}

    # Act
    result1 = atualizar_produto(1, ProdutoPatchReq(**update1)).dict()

    # Assert
    assert result1["antes"]["dicionario"] == {"chave1": "valor1"}
    assert result1["depois"]["dicionario"] == {"chave1": "valor1", "chave2": "valor2"}

def test_deletar_produto():
    # Arrange
    mongo.coll.delete_many({})

    doc1 = {"nome": "Banana",
            "preco": Decimal("1.99"),
            "descricao": "Algumas bananas"}
    cadastrar_produto(Produto(**doc1))

    # Act
    result1 = deletar_produto(1).dict()

    # Assert
    assert result1["deletado"]["nome"] == "Banana"
    assert result1["deletado"]["preco"] == Decimal("1.99")
    assert result1["deletado"]["descricao"] == "Algumas bananas"
    assert mongo.coll.count_documents({}) == 0
    assert listar_produtos() == []