from decimal import Decimal
from pydantic import BaseModel, Field, root_validator, validator


class Produto(BaseModel):
    doc_id: int = Field(1, ge=1)
    nome: str = Field(..., min_length=1, max_length=30)
    preco: Decimal = Field(..., ge=0, decimal_places=2)
    descricao: str = Field(..., min_length=1, max_length=200)

    @root_validator(pre=True)
    def float_to_decimal(cls, values: dict):
        return values | {k: Decimal(v).quantize(Decimal("0.00"))
                         for k, v in values.items()
                         if isinstance(v, float)}

    @validator("preco")
    def format_currency(cls, v):
        return Decimal(v).quantize(Decimal("0.00"))

    class Config:
        anystr_strip_whitespace = True
        extra = "allow"

class ProdutoPatchReq(BaseModel):
    nome: str | None = Field(min_length=1, max_length=30)
    preco: Decimal | None = Field(ge=0, decimal_places=2)
    descricao: str | None = Field(min_length=1, max_length=200)

    class Config:
        anystr_strip_whitespace = True
        extra = "allow"

class ProdutoResponse(BaseModel):
    antes: Produto | None
    depois: Produto | None
    deletado: Produto | None

## TODO: converter floats dentro de lists, dicts, etc. para Decimals