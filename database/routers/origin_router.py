from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_417_EXPECTATION_FAILED, HTTP_400_BAD_REQUEST

from parser.core.dtos.origin_dto import OriginDTO
from parser.exceptions import AlreadyExistError
from parser.routers.router_depends import IOriginService

router = APIRouter(prefix="/origins", tags=["origins"])


# @router.get("", response_model=list[UserCreate])
# async def get_users_origins(session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
#     origins = await origins_crud.get_all_users(session=session)
#     return users


@router.post("", response_model=OriginDTO, status_code=HTTP_201_CREATED)
async def create_user(service: IOriginService, origin: OriginDTO):
    """"Эндпоинт регистрации пользователя"""
    try:
        return await service.create(dto=origin)
    except AlreadyExistError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
