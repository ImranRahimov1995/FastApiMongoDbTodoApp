from fastapi import APIRouter, HTTPException, status
from pymongo import errors

from src.schemas.user_schema import UserAuth, UserOut
from src.services.user_service import UserService

user_router = APIRouter()


@user_router.post('/create',
                  summary="Create new user",
                  response_model=UserOut,
                  status_code=status.HTTP_201_CREATED)
async def create_user(data: UserAuth):
    try:

        user = await UserService.create_user(data)
        return user

    except errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User with this email or username is exists'
        )
