from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange



class Post(BaseModel):
    name:str
    email:str
    is_student: bool = False
    rating: Optional[int] = None
    


app = FastAPI()

my_posts = [
    { "name":"kassu melkassa","email":"kassu@gmail.com","is_student":True,"rating":5,"id":200},
    { "name":"abdisa","email":"abdisa@gmail.com","is_student":True,"rating":10,"id":100}
    ]

def find(id):
    for p in my_posts:
        if p['id'] == id:
            return p

#findd = [p['id'] ==id for p in my_posts ]

#function to return the index
def find_index_post(id):
    for x, y in enumerate(my_posts):
        if y['id'] == id:
            return x



@app.get("/")
def root():
    return {"data": "welcome to my api"} 

@app.get("/posts")
def get_posts():
    return {'data':my_posts}

@app.post("/posts", status_code=status.HTTP_202_ACCEPTED)
def create_posts(post: Post):
    print(post.rating) ## this is regular pydantic model
    global post_dict
    post_dict = post.dict() # this enables us to change pydantic model to dictionary
    post_dict['id'] = randrange(1, 1000)
    my_posts.append(post_dict)
    return {"data":post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response:Response):
    post = find(int(id))
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} was not found!'
        )
    return {"post_detail":post}

@app.delete("/posts/{id}")
def delete_post(id: int):
   
   index = find_index_post(id)
   if index == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} was not found!')
   my_posts.pop(index)
   return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    
    index = find_index_post(id)
    if index == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id {id} was not found!')
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    
    
    return {"data":post_dict}
    