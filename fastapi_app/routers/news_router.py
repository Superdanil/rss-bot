from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from core.dtos import NewsCreateDTO, NewsResponseDTO
from routers.router_depends import INewsService

router = APIRouter(prefix="/news", tags=["news"])


@router.post("", status_code=HTTP_201_CREATED)
async def create_news(service: INewsService, dto_list: list[NewsCreateDTO]):
    """Эндпоинт добавления новостей в БД"""
    await service.add_news(dto_list=dto_list)
    return JSONResponse("ОК")


@router.get("", response_model=list[NewsResponseDTO], status_code=HTTP_200_OK)
async def get_users_news(service: INewsService, telegram_id: int, hours: int):
    """Возвращает новостную ленту пользователя за количество часов hours"""
    return await service.get_users_news(telegram_id, hours)
