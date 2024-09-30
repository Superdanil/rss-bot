from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from routers import router as user_router
from core.settings import settings
from core.models import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    # async with db_helper.engine.begin() as conn:
    # await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(title="Сервис мониторинга новостей", default_response_class=ORJSONResponse, lifespan=lifespan)
    app.include_router(user_router)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.PARSER_HOST, port=settings.PARSER_PORT, reload=True)
