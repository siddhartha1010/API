from typing import Optional,Union
from fastapi import APIRouter,status,Response
from enum import Enum

router=APIRouter(
    prefix='/blog',
    tags=['blog']
)

class ModelName(str, Enum):
    alexnet = "alex"
    resnet = "resnet"
    lenet = "lenet"

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = "haha"):
    return {"item_id": item_id, "q": q}


# @app.get("/itemss/{id}")
# def all_items(id:int):
#     return {"message":f"All items are found with {id}"}
    
# @app.get("/items/type/{type}")
# def types(type: ModelName):
#     return {"message":f"All items are found with {type}"}

@router.get('/{blog_id}/comments/{comment_id}',tags=['comment','blog'])
def get_comment(blog_id:int, comment_id:int,username:Optional[str]=None):
    return {"message":f"blog {blog_id} {comment_id},username: {username}"}


@router.get('/{id}',tags=['blog'])
def get_blog(id:int,response:Response):
    if id>5:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"error":f"Id not found",}
    else:
        response.status_code=status.HTTP_200_OK
        return {"message":f"blog {id} found"}
         
