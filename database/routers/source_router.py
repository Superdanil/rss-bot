from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import ValidationError
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from database.core.dtos import SourceReadDTO
from database.core.dtos.user_source_dto import UserSourceDTO
from database.routers.router_depends import ISourceService, get_user_interactor
from database.services import UserInteractor

router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("", response_model=list[SourceReadDTO], status_code=HTTP_200_OK)
async def get_all_sources(service: ISourceService, limit: int = 50, offset: int = 0):
    """Возвращает список всех источников"""
    try:
        return await service.get_source_list(limit, offset)
    except Exception as e:
        print(e)


# @router.get("", response_model=list[SourceDTO])
# async def get_users_sources(telegram_id: int, service: ISourceService):
#     """Возвращает список подписок пользователя."""
#     try:
#         return await service.get_users_sources(dto=dto)
#     except AlreadyExistError as e:
#         raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("", status_code=HTTP_200_OK)
async def create_source_relation(
        dto: UserSourceDTO,
        interactor: Annotated[UserInteractor, Depends(get_user_interactor)]
) -> JSONResponse:
    """Эндпоинт регистрации источника новостей"""
    try:
        await interactor.add_or_get_association(dto=dto)
    except ValidationError:
        pass
    return JSONResponse("Источник успешно добавлен")
