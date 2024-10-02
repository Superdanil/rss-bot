from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .router_depends import INewsService
from ..core.dtos.user_dto import UserCreateDTO
from ..exceptions import AlreadyExistError

router = APIRouter(prefix="/news", tags=["news"])


@router.post("", response_model=UserCreateDTO, status_code=HTTP_201_CREATED)
async def create_news(service: INewsService, user_create: UserCreateDTO):
    """"Эндпоинт добавления новости в БД"""
    try:
        return await service.create(dto=user_create)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
