from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import ValidationError
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK

from core.dtos import SourceReadDTO
from core.dtos.user_source_dto import UserSourceDTO
from routers.router_depends import ISourceService, get_user_interactor
from services import UserInteractor

router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("", response_model=list[SourceReadDTO], status_code=HTTP_200_OK)
async def get_all_sources(service: ISourceService, limit: int = 50, offset: int = 0):
    """Возвращает список всех источников"""
    try:
        return await service.get_source_list(limit, offset)
    except Exception as e:
        print(e)


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
