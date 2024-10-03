from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from database.core.dtos import UserReadDTO
from database.core.dtos.user_dto import UserCreateDTO
from database.exceptions import AlreadyExistError
from database.routers.router_depends import IUserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserReadDTO, status_code=HTTP_201_CREATED)
async def create_user(service: IUserService, dto: UserCreateDTO):
    """Эндпоинт регистрации пользователя"""
    try:
        return await service.add_or_get_user(telegram_id=dto.telegram_id)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
