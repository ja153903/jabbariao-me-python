from fastapi import FastAPI

from .posts.api import router as post_router

app = FastAPI()

app.include_router(post_router)