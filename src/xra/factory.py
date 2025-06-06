from fastapi import FastAPI
from xra.routes import math


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(math.router, prefix="/math", tags=["Math"])
    return app
