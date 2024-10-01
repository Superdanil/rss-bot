from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from parser.core.dtos.user_dto import UserCreateDTO
from parser.exceptions import AlreadyExistError
from parser.routers.router_depends import IUserService

router = APIRouter(prefix="/news", tags=["news"])


@router.post("", response_model=UserCreateDTO, status_code=HTTP_201_CREATED)
async def create_news(service: IUserService, user_create: UserCreateDTO):
    """"Эндпоинт регистрации пользователя"""
    try:
        return await service.create(dto=user_create)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
