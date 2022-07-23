from typing import Optional
from uuid import UUID

from src.schemas.user_schema import UserAuth
from src.models.user_model import User
from src.core.security import get_password, verify_password


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)

        if not user:
            return None

        if not verify_password(password, hashed_pass=user.hashed_password):
            return None

        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)

        return user

    @staticmethod
    async def get_user_by_id(user_id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == user_id)

        return user
