from fastapi import APIRouter , HTTPException , status ,Depends
from typing import List
from sqlalchemy.orm import Session
from ..bcrypt import Password
from ..database import get_db
from .. import models, schemas


router = APIRouter(prefix='/user',tags=['Users'])

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
def get_all_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Users Found")

    return users

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    new_user = models.User(email=request.email,password=Password.encrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowUser)
def get_user(id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No User Found")
    
    return user
