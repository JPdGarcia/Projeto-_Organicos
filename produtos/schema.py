post = {
    "required": {
        "summary": "Campos obrigatórios",
        "description": """Os campos `nome`, `preco`, e `descricao` são obrigatórios.

`nome`: Uma `str` com no mínimo um caracter, e no máximo 30.

`preco`: Uma `int` ou `float` positiva. Se `float`, deve ter no máximo duas casas decimais.

`description`: Uma `str` com no mínimo um caracter, e no máximo 200.""",
        "value": {
            "nome": "Banana",
            "preco": 1.99,
            "descricao": "Um cacho de bananas."
        }
    },
    "extra": {
        "summary": "Campos adicionais",
        "description": "Campos extras, contendo outros tipos de dados, também podem ser inclusos.",
        "value": {
            "nome": "Maçã",
            "preco": 2.00,
            "descricao": "Um kilo de maçãs.",
            "dados": {
                "estoque": 35,
                "fornecedores": [
                    "Fazenda do Ettore",
                    "Fazenda do Osiel"
                ],
                "preco_desconto": 1.99
            }
        }
    }
}

patch = {
    "example": {
        "summary": "Exemplo de campos.",
        "description": """Todos os campos são opcionais.

Se um for incluso e existir no documento selecionado, o valor do campo no documento será mudado para o valor providenciado. Se o campo não existir no documento, ele será criado.""",
        "value": {
            "nome": "Goiaba",
            "descricao": "Um kilo de goiabas.",
        }
    }
}