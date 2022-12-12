from decimal import Decimal
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4


class Produto(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id",
                     example="12345678-1234-5678-1234-567812345678")
    nome: str = Field(..., example="Banana")
    preco: Decimal = Field(..., ge=0, decimal_places=2, example=Decimal("4.18"))
    descricao: str = Field(..., example="Uma dúzia de bananas.")

    @validator("preco")
    def currency_validator(cls, v):
        return Decimal(v).quantize(Decimal("0.00"))

    class Config:
        anystr_strip_whitespace = True
        extra = "allow"
        allow_population_by_field_name = True

class ProdutoPatchReq(BaseModel):
    nome: str | None = Field(example="Maçã")
    preco: Decimal | None = Field(ge=0, decimal_places=2, example=Decimal("2.00"))
    descricao: str | None = Field(example="Um kilo de maçãs.")

    class Config:
        anystr_strip_whitespace = True
        extra = "allow"
        fields = {"_id": {"exclude": True},
                  "id": {"exclude": True}}

class ProdutoResponse(BaseModel):
    antes: Produto | None
    depois: Produto | None
    deletado: Produto | None