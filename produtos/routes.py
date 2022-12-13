from fastapi import APIRouter, HTTPException, Body

from database import mongo
from models import Produto, ProdutoPatchReq, ProdutoResponse
import schema


router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("/", status_code=200, response_model=list[Produto])
def listar_produtos():
    return list(mongo.coll.find(projection={"_id": False}))


@router.get("/{doc_id}", status_code=200, response_model=Produto)
def listar_um_produto(doc_id: int):
    if doc := mongo.coll.find_one(
            filter={"doc_id": doc_id},
            projection={"_id": False}):
        return doc

    raise HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.post("/", status_code=201, response_model=Produto)
def cadastrar_produto(produto: Produto = Body(examples=schema.post)):
    produto.doc_id = mongo.coll.count_documents({}) + 1
    new_doc = produto.dict(exclude={"_id": True})

    if mongo.coll.find_one({k:v for k,v in new_doc.items() if k != "doc_id"}):
        raise HTTPException(400, "Este produto já está cadastrado")

    result = mongo.coll.insert_one(new_doc)
    inserted_doc = mongo.coll.find_one(
        filter={"_id": result.inserted_id},
        projection={"_id": False})

    return inserted_doc


@router.patch(
    "/{doc_id}",
    status_code=200,
    response_model=ProdutoResponse,
    response_model_exclude_unset=True)
def atualizar_produto(doc_id: int, produto: ProdutoPatchReq = Body(examples=schema.patch)):
    new_values = produto.dict(exclude={"_id": True, "doc_id": True}, exclude_unset=True)

    if doc_before := mongo.coll.find_one_and_update(
            filter={"doc_id": doc_id},
            update={"$set": new_values},
            projection={"_id": False}):
        doc_after = mongo.coll.find_one(
            filter={"doc_id": doc_id},
            projection={"_id": False})
        return ProdutoResponse(antes=doc_before, depois=doc_after)
    
    raise HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.delete(
    "/{doc_id}",
    status_code=200,
    response_model=ProdutoResponse,
    response_model_exclude_unset=True)
def deletar_produto(doc_id: int):
    if deleted_doc := mongo.coll.find_one_and_delete(
            filter={"doc_id": doc_id},
            projection={"_id": False}):
        return ProdutoResponse(deletado=deleted_doc)
    
    raise HTTPException(404, f"Produto com o ID {doc_id} não foi deletado, pois não existe")
