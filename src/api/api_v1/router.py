from fastapi import APIRouter
from src.api.api_v1.handlers import user
from src.api.auth import jwt

router = APIRouter()

# http://127.0.0.1:8000/api/v1/users/test
router.include_router(user.user_router, prefix='/users', tags=['users'])
router.include_router(jwt.auth_router,prefix='/auth',tags=['auth'])