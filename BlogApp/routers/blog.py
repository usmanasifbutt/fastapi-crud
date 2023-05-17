
from fastapi import APIRouter,status, Depends , HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, models, oauth2

router =  APIRouter()

@router.post('/blog',status_code=status.HTTP_201_CREATED,tags=['Blogs'])
def create(request: schemas.BlogBase, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/blog', response_model=List[schemas.ShowBlog],tags=['Blogs'])
def index(db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Blogs Found")
    return blogs


@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog,tags=['Blogs'])
def show(id, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'No Blog Found with id {id}')
    
    return blog


@router.patch('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def update(id, request: schemas.BlogBase, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'No Blog Found with id {id}')
    
    blog.update(request.dict())
    db.commit()
    return {"message": f"Blog updated Succesfully"}


@router.delete('/blog/{id}', status_code=status.HTTP_200_OK,tags=['Blogs'])
def destroy(id, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'No Blog Found with id {id}')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": f'Blog with id:{id} is deleted'}
