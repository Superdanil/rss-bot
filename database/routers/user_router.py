from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from database.core.dtos.user_dto import UserCreateDTO
from database.exceptions import AlreadyExistError
from database.routers.router_depends import IUserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserCreateDTO, status_code=HTTP_201_CREATED)
async def create_user(service: IUserService, user_create: UserCreateDTO):
    """"Эндпоинт регистрации пользователя"""
    try:
        return await service.create(dto=user_create)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
