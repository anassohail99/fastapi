"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.firebase import initialize_firebase
from app.core.config import settings
# from app.core.logging_config import init_logging


from app.routes import (
    auth_router,
)


# configure loggins
# init_logging()
# logger = logging.getLogger(__name__)


# initialize firebase
initialize_firebase()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO: Include routers: auth, portfolio, upload, public
# from app.auth.routes import router as auth_router
# from app.routes.portfolio import router as portfolio_router
# from app.routes.upload import router as upload_router
# from app.routes.public import router as public_router
# app.include_router(auth_router, prefix="/auth", tags=["auth"])
# app.include_router(portfolio_router, prefix="/portfolio", tags=["portfolio"])
# app.include_router(upload_router, prefix="/upload", tags=["upload"])
# app.include_router(public_router, prefix="/public", tags=["public"])
