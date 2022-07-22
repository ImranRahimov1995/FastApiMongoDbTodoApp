from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings
from src.models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.on_event("startup")
async def app_init():
    """
        initialize crucial application services
    """

    # init db client , fodoist is app name nothing else
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).fodoist

    await  init_beanie(
        database=db_client,
        document_models=[
            User,
        ]
    )

# Run command
# uvicorn src.app:app --reload
