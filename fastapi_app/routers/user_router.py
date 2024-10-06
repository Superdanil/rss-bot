from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from core.dtos.user_dto import UserCreateDTO
from routers.router_depends import IUserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=HTTP_200_OK)
async def create_user(service: IUserService, dto: UserCreateDTO):
    """Эндпоинт регистрации пользователя"""
    await service.add_or_get_user(telegram_id=dto.telegram_id)
    return JSONResponse("ОК")
