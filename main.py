from fastapi import FastAPI
from BookModule.Model.book_model import Book
from UserModule.Model.user_model import User
from BorrowModule.Model.borrow_model import Borrow
from database_environnement import Base, engine
from UserModule.Router.user_routers import user_router
from BookModule.Router.book_routers import book_router
from BorrowModule.Router.borrow_routers import borrow_router
from fastapi import APIRouter

Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(book_router)
app.include_router(borrow_router)

@app.get("/")
def welcome():
    return {"Message" : "Bienvenue sur mon api de gestion de livre"}