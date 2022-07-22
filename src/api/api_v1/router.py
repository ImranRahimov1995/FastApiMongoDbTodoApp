from fastapi import APIRouter
from src.api.api_v1.handlers import user

router = APIRouter()

# http://127.0.0.1:8000/api/v1/users/test
router.include_router(user.user_router, prefix='/users', tags=['users'])
