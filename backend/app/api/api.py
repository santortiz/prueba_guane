from fastapi import APIRouter


from app.api.routers import (
    root,
    enterprise,
    user

)

api_router = APIRouter()
api_router.include_router(root.router, prefix="/health-check", tags=["Health check"])
api_router.include_router(enterprise.router, prefix="/enterprises", tags=["enterprises"])
api_router.include_router(user.router, prefix="/users", tags=["users"])