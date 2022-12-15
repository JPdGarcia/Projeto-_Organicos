from fastapi import APIRouter, HTTPException, Body

from database import mongo
from models import Produto, ProdutoPatchReq, ProdutoResponse
import schema


router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("/", status_code=200, response_model=list[Produto])
def listar_produtos():
    find_result = mongo.coll.find(projection={"_id": False})

    return list(find_result)


@router.get("/{doc_id}", status_code=200, response_model=Produto)
def listar_um_produto(doc_id: int):
    args = {
        "filter": {"doc_id": doc_id},
        "projection": {"_id": False}}

    if find_result := mongo.coll.find_one(**args):
        return find_result

    raise HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.post("/", status_code=201, response_model=Produto)
def cadastrar_produto(produto: Produto = Body(examples=schema.post)):
    produto.doc_id = mongo.coll.count_documents({}) + 1
    new_doc = produto.dict(exclude={"_id": True})

    insert_result = mongo.coll.insert_one(new_doc)
    args = {
        "filter": {"_id": insert_result.inserted_id},
        "projection": {"_id": False}}

    inserted_doc = mongo.coll.find_one(**args)
    return inserted_doc


@router.patch("/{doc_id}", status_code=200,
              response_model=ProdutoResponse, response_model_exclude_unset=True)
def atualizar_produto(doc_id: int, produto: ProdutoPatchReq = Body(examples=schema.patch)):
    new_values = produto.dict(exclude={"_id": True, "doc_id": True}, exclude_unset=True)

    args = {
        "filter": {"doc_id": doc_id},
        "projection": {"_id": False}}

    if doc_before := mongo.coll.find_one_and_update(**args, update={"$set": new_values}):
        doc_after = mongo.coll.find_one(**args)
        return ProdutoResponse(antes=doc_before, depois=doc_after)
    
    raise HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.delete("/{doc_id}", status_code=200,
               response_model=ProdutoResponse, response_model_exclude_unset=True)
def deletar_produto(doc_id: int):
    args = {
        "filter": {"doc_id": doc_id},
        "projection": {"_id": False}}

    if deleted_doc := mongo.coll.find_one_and_delete(**args):
        return ProdutoResponse(deletado=deleted_doc)
    
    raise HTTPException(404, f"Produto com o ID {doc_id} não foi deletado, pois não existe")

## TODO: expandir funcionalidade de updates