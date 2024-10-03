from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from database.core.dtos import NewsDTO
from database.exceptions import AlreadyExistError
from database.routers.router_depends import INewsService

router = APIRouter(prefix="/news", tags=["news"])


@router.post("", response_model=NewsDTO, status_code=HTTP_201_CREATED)
async def create_news(service: INewsService, dto: NewsDTO):
    """Эндпоинт добавления новости в БД"""
    try:
        return await service.create(dto=dto)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
