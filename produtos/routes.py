from fastapi import APIRouter, HTTPException, Body
from uuid import UUID

from database import mongo
from models import Produto, ProdutoPatchReq, ProdutoResponse


router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("/", status_code=200, response_model=list[Produto])
def listar_produtos():
    return list(mongo.coll.find())


@router.get("/{doc_id}", status_code=200, response_model=Produto)
def listar_um_produto(doc_id: UUID):
    if doc := mongo.coll.find_one({"_id": doc_id}):
        return doc

    raise HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.post("/", status_code=201, response_model=Produto)
def cadastrar_produto(produto: Produto = Body(example={"nome": "Banana",
                                                       "preco": "4.18",
                                                       "descricao": "Uma dúzia de bananas."})):
    new_doc = produto.dict(by_alias=True)

    if mongo.coll.find_one({k:v for k,v in new_doc.items() if k != "_id"}):
        raise HTTPException(400, "Este produto já está cadastrado")

    result = mongo.coll.insert_one(new_doc)
    inserted_doc = mongo.coll.find_one({"_id": result.inserted_id})

    return inserted_doc


@router.patch("/{doc_id}",
              status_code=200,
              response_model=ProdutoResponse,
              response_model_exclude_unset=True)
def atualizar_produto(doc_id: UUID, produto: ProdutoPatchReq):
    produto = produto.dict(exclude={"_id": True, "id": True}, exclude_unset=True)

    if doc_before := mongo.coll.find_one_and_update({"_id": doc_id}, {"$set": produto}):
        doc_after = mongo.coll.find_one({"_id": doc_id})
        return ProdutoResponse(antes=doc_before, depois=doc_after)
    
    raise HTTPException(404, f"Produto com o ID {doc_id} não existe")


@router.delete("/{doc_id}",
               status_code=200,
               response_model=ProdutoResponse,
               response_model_exclude_unset=True)
def deletar_produto(doc_id: UUID):
    if deleted_doc := mongo.coll.find_one_and_delete({"_id": doc_id}):
        return ProdutoResponse(deletado=deleted_doc)
    
    raise HTTPException(404, f"Produto com o ID {doc_id} não foi deletado, pois não existe")


# TODO: figure out how to forbid _id setting during requests to /cadastrar