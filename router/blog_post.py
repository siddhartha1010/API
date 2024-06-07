from fastapi import APIRouter,Query,Body,Path,Depends
from typing import Optional,List
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    body: str
    # published:Optional[bool]
    published:Optional[bool]=None

# @router.post('/new')
# def create(blog:BlogModel):
#     return {'data':blog}

@router.post('/new/{id}')
def create_blog(blog:BlogModel, id:int,version:int=1):
    return{
        'id':id,
        "data":blog,
        'version':version

    }
def importing_this_functionality():
    return {'Message':'This was imported from importing_this_functionality'}
@router.post('/new/{id}/comment/{comment_id}')#path parameters
def create_comment(blog:BlogModel, id:int,comment_title:int=Query(#Query parameters
    None,#Query parameters is optional
    title='title of the comment',#Doesnt show as of now
    description='some reandom comment description',
    alias='comment title',#used to specify an alternative name for a parameter in the API request.
    deprecated=True#used to indicate that a particular parameter (or endpoint) is considered outdated and should not be used in new code.
),
    # content:str = Body('hi how are you doing')#Default value is optional
    content:str = Body(...,
                       min_length=10,
                       max_length=12, 
                       regex='^[a-z\s]*$'#regular expression for small letters and space no large letters

                       ),#This is not optional must be provided is called
    # content:str = Body(Ellipsis)#This is not optional must be provided
    v: Optional[List[str]] = Query(None),#List is imported from typing
    # comment_id: int =Path(None, gt=5, le=10)
    comment_id: int =Path(..., gt=5, le=10),
    required_parameters: dict = Depends(importing_this_functionality)

):
    return{  #response
        'blog':blog, 
        'id':id,
        'comment_title':comment_title,
        'content':content,
        'version':v,
        'comment_id':comment_id, 
        'req':required_parameters
    }   


