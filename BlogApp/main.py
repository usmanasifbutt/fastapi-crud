from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from . import  models
from .database import engine
from .routers import user, blog, auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(blog.router)
