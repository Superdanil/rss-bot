from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK

from database.core.dtos import NewsCreateDTO, NewsReadDTO
from database.exceptions import AlreadyExistError
from database.routers.router_depends import INewsService

router = APIRouter(prefix="/news", tags=["news"])


@router.post("", response_model=list[NewsCreateDTO], status_code=HTTP_201_CREATED)
async def create_news(service: INewsService, dto_list: list[NewsCreateDTO]):
    """Эндпоинт добавления новостей в БД"""
    try:
        return await service.add_news(dto_list=dto_list)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("", response_model=list[str], status_code=HTTP_200_OK)
async def get_users_news(service: INewsService, timedelta: int):
    """"""
    try:
        return await service.get_source_list(limit, offset)
    except Exception as e:
        print(e)
