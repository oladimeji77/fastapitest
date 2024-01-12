from fastapi import Response, status, HTTPException, Depends, APIRouter
from models import Dog


router = APIRouter(prefix="/buy", tags=['Buy'])

@router.get("/{id}")
async def index(id:int):
    return {"message":f" your ID  is: {id}"}
 
@router.post("/")  #you can psot from the swagger
async def breed(dog:Dog):
    return dog