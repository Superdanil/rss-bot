from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from routers.router_depends import ISourceService, get_user_interactor
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from core.dtos import SourceReadDTO
from core.dtos.user_source_dto import UserSourceDTO
from services import UserInteractor

router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("", response_model=list[SourceReadDTO], status_code=HTTP_200_OK)
async def get_all_sources(service: ISourceService, limit: int = 50, offset: int = 0):
    """Возвращает список всех источников"""
    return await service.get_source_list(limit, offset)


@router.post("", status_code=HTTP_200_OK)
async def create_source_relation(
        dto: UserSourceDTO, interactor: Annotated[UserInteractor, Depends(get_user_interactor)],
) -> JSONResponse:
    """Эндпоинт регистрации источника новостей"""
    await interactor.add_or_get_association(dto=dto)
    return JSONResponse("Источник успешно добавлен")
