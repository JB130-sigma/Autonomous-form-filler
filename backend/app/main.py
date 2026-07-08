#from app.core.security import hash_password, verify_password
from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.core.config import settings
from app.core.logging import logger
from app.db.__init__db import init_db

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(auth_router)


@app.on_event("startup")
def startup():
    logger.info("Initializing Database...")
    init_db()
    logger.info("Database Initialized Successfully!")

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "debug": settings.DEBUG,
    }


#@app.get("/test-password")
#def test_password():
#
#    password = "Jeet@123"
#
#    hashed = hash_password(password)
#
#    verified = verify_password(password, hashed)
#
#    return {
#        "password": password,
#        "hash": hashed,
#        "verified": verified
#    }
#from app.core.security import (
#    create_access_token,
# #   decode_access_token,
#)


#@app.get("/test-token")
#d#ef test_token():
#
#    token = create_access_token(
#        {"sub": "1"}
#    )
#
#    payload = decode_access_token(token)
#
# #   return {
#        "token": token,
#        "payload": payload,
#    }
